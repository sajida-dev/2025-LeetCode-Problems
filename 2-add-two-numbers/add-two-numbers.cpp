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
        int n=0,q=0;
        ListNode* start;
        n = l1->val+l2->val;
        if( n>9 )
        {
            q = n%10;
            n = n/10;
        }else{
            q = n;
            n=0;
        }
        
        ListNode* l3 = new ListNode(q);
        start = l3;
         l1 = l1->next;
         l2 = l2->next;
        while(l1!=NULL || l2!=NULL)
        {
            int x=0,y=0;
            if(l1!=NULL)
            {
                x = l1->val;
                l1 = l1->next;
            }
            if(l2!=NULL)
            {
                y = l2->val;
                l2 = l2->next;
            }
            cout << "value of n : " << n << " ||";
            n=x+y+n;
            cout << "value of n : " << n << " ||";
            if( n>9 )
            {
                q = n%10;
                n = n/10;
            }else{
                q = n;
                n=0;
            }
            l3->next = new ListNode(q);
            cout << l3->val << " || ";
            l3 = l3->next;
        }
        if(n!=0)
        {
            l3->next = new ListNode(n);
        }
        return start;
    }
};