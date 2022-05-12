#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

struct node{
    int val;
    struct node *left, *right;
};

bool containsDuplicate(int *, int);
struct node * insertIntoTree(struct node *, int);
struct node* createNewNode(int);

bool containsDuplicate(int* nums, int numsSize){
    if(numsSize < 1)
        return false;
    int i;
    struct node *root = NULL;
    root = insertIntoTree(root, *nums);
    for(i=1, nums++; i<numsSize ; i++,nums++){
        if(insertIntoTree(root, (int)*nums) == NULL)
            return true;
    }
    return false;
    
}

struct node* createNewNode(int val){
    struct node* newNode = (struct node*)malloc(sizeof(struct node));
    newNode -> left = NULL;
    newNode -> right = NULL;
    newNode -> val = val;
    return newNode;
}

struct node* insertIntoTree(struct node *root, int val){
    if(root == NULL){
        return createNewNode(val);
    }
    
    //Recursively try to insertIntoTree
    if(root->val == val) 
        return NULL;
    else if(root->val > val){
        struct node *temp = insertIntoTree(root->left, val);
        if(temp == NULL)
            return NULL;
        else
            root->left = temp;
    }
    else{
        struct node *temp = insertIntoTree(root->right, val);
        if(temp == NULL)
            return NULL;
        else
            root->right = temp;
    }
    return root;
}

int main(){
    int nums[] = {1,2,3,4,1,5,6};
    printf("Duplicate present? %s", containsDuplicate(nums, 6) ? "true" : "false");
    return 1;
}