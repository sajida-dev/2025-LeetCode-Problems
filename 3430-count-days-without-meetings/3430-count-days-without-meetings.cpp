class Solution {
public:
    int countDays(int days, vector<vector<int>>& meetings) {
        int count=0,start=1,end=0;
        sort(meetings.begin(),meetings.end());
        start = 1;
        for(int i=0; i<meetings.size(); i++)
        {
            if(start < meetings[i][0])
            {
                count+=((meetings[i][0])-start);
            }
            if(start<meetings[i][1]+1)
            {
                start = meetings[i][1]+1;
            }
            
        }
        if(days>start)
        {
            count+=(days-(start));
            start += (days-(start));
        }
        if(days==start)
        {
            count++;
        }
        return count;
    }
};