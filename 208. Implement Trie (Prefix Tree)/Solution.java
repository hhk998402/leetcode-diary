class Node {
    Map<Character, Node> children;
    boolean isWord;

    public Node(){
        this.children = new HashMap();
        this.isWord = false;
    }

    public void addChild(Character ch, Node node){
        this.children.put(ch, node);
    }

    public void setWord(){
        this.isWord = true;
    }

    public Node getChild(Character ch){
        return this.children.containsKey(ch) ? this.children.get(ch) : null;
    }

    public boolean isWord(){
        return this.isWord;
    }
}

class Trie {

    Node node;

    public Trie() {
        node = new Node();
    }
    
    public void insert(String word) {
        Node ptr = node;
        int len = 0;
        int n = word.length();
        for(Character ch : word.toCharArray()){
            if(ptr.getChild(ch) != null){
                ptr = ptr.getChild(ch); 
            } else{
                Node newNode = new Node();
                ptr.addChild(ch, newNode);
                ptr = newNode;
            }
            if(len == n-1){
                ptr.setWord();
            }
            len += 1;
        }
    }
    
    public boolean search(String word) {
        Node ptr = node;
        int len = 0;
        int n = word.length();
        for(Character ch : word.toCharArray()){
            if(ptr.getChild(ch) == null){
                return false;
            }
            ptr = ptr.getChild(ch);
            if(len == n-1){
                if(ptr.isWord()){
                    return true;
                }
                break;
            }
            len += 1;
        }
        return false;
    }
    
    public boolean startsWith(String prefix) {
        Node ptr = node;
        int len = 0;
        int n = prefix.length();
        for(Character ch : prefix.toCharArray()){
            if(ptr.getChild(ch) == null){
                return false;
            }
            ptr = ptr.getChild(ch);
            if(len == n-1){
                break;
            }
            len += 1;
        }
        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */