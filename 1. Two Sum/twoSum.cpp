#include <unordered_map>
#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> indices(2,0);
        unordered_map<int, int> hmap;
        int currIdx = 0;
        int key = 0;
        for(vector<int>::iterator it = nums.begin(); it != nums.end(); it++, currIdx++){
            key = target - it[0];
            if(hmap.find(it[0]) != hmap.end()){ //Found key
                indices[0] = hmap[it[0]];
                indices[1] = currIdx;
                cout<<"Here"<<currIdx<<";"<<endl;
                break;
            } else{
                hmap[key] = currIdx;
            }
        }
        return indices;
    }
};