/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int carry = 0;
        int sum = 0;
        int lval = 0;
        int rval = 0;
        ListNode *head, *tail, *newNode;
        bool firstIteration = true;
        while(l1 != nullptr || l2 != nullptr){
            if(l1 != nullptr){
                lval = l1->val;
            } else{
                lval = 0;
            }
            if(l2 != nullptr){
                rval = l2->val;
            } else{
                rval = 0;
            }
            // cout<<sum<<'\t'<<lval<<'\t'<<rval<<endl;
            sum = lval + rval + carry;
            if(sum > 9){
                carry = 1;
            } else{
                carry = 0;
            }
            newNode = new ListNode(sum%10, nullptr);
            // newNode->val = sum%10;
            // newNode->next = nullptr;
            if(firstIteration){
                firstIteration = false;
                head = newNode;
                head->next = nullptr;
            } else{
                if(head->next == nullptr){
                    tail = newNode;
                    head->next = newNode;
                } else{
                    tail->next = newNode;
                    tail = tail->next;
                    tail->next = nullptr;
                }
            }
            
            l1 = l1 == nullptr || l1->next == nullptr ? nullptr : l1->next; 
            l2 = l2 == nullptr || l2->next == nullptr ? nullptr : l2->next;
            cout<<sum<<((l1 != nullptr || l2 != nullptr) ? "true": "false")<<'\t'<<(head->val)
                <<'\t'<<(head->next ? head->next->val : -99)<<endl;
        }
        if(carry!=0){
            newNode = new ListNode(carry%10, nullptr);
            if(head->next == nullptr){
                tail = newNode;
                head->next = newNode;
            } else{
                tail->next = newNode;
                tail = tail->next;
                tail->next = nullptr;
            }
        }
        cout<<"Exited"<<endl;
        ListNode *temp;
        for(temp = head; temp != nullptr; temp = temp->next){
            cout<<endl<<temp->val<<"->";
        }
        return head;
    }
};