class Solution {
public:
    string clearDigits(string s) {
        for(int i=0; i<s.size(); i++)
        {
            if(isdigit(s[i]))
            {
                s.erase(s.begin()+i);
                i--;
                s.erase(s.begin()+i);
                i--;
            }
        }
        return s;
    }
};