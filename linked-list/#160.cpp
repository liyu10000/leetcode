// brute force compare
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if (headA == NULL || headB == NULL)
            return NULL;
        ListNode *currA = headA;
        while (currA != NULL) {
            ListNode *currB = headB;
            while (currB != NULL) {
                if (currA == currB)
                    return currA;
                else
                    currB = currB->next;
            }
            currA = currA->next;
        }
        return NULL;
    }
};

// count length
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if (!headA || !headB) return NULL;
        // get tail node and count # of nodes
        ListNode *currA = headA;
        ListNode *currB = headB;
        int cntA = 1, cntB = 1;
        while (currA->next) {
            cntA++;
            currA = currA->next;
        }
        while (currB->next) {
            cntB++;
            currB = currB->next;
        }
        // no intersect if tail nodes are different
        if (currA != currB) return NULL;
        // skip some nodes to start with same length
        currA = headA;
        currB = headB;
        int skip = abs(cntA - cntB);
        if (cntA > cntB) {
            while (skip > 0) {
                currA = currA->next;
                skip--;
            }
        } else if (cntA < cntB) {
            while (skip > 0) {
                currB = currB->next;
                skip--;
            }
        }
        // compare
        while (currA != currB) {
            currA = currA->next;
            currB = currB->next;
        }
        return currA;
    }
};