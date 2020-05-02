#include <bits/stdc++.h>
using namespace std;

string xx;
int NUM_VARS, NUM_CLAUSES;
vector<vector<int> > clauses;

int main() {
    
    cin >> xx >> xx >> NUM_VARS >> NUM_CLAUSES;
    for (int i = 0; i < NUM_CLAUSES; i++) {
        int var;
        vector<int> clause;
        while (cin >> var) {
            if (var == 0) break;
            clause.push_back(var);
        }
        clauses.push_back(clause);
    }
    
    int num_solns = 0;
    for (int i = 0; i < (1 << NUM_VARS); i++) {
        bool valid = true;
        for (int j = 0; j < clauses.size(); j++) {
            bool ok = false;
            for (int k = 0; k < clauses[j].size(); k++) {
                if (clauses[j][k] < 0 && ((1 << abs(clauses[j][k]) - 1) & i) == 0) {
                    ok = true;
                    break;
                }
                if (clauses[j][k] > 0 && ((1 << abs(clauses[j][k]) - 1) & i) > 0) {
                    ok = true;
                    break;
                }
            }
            if (!ok) {
                valid = false;
                break;
            }
        }
        if (valid) num_solns++;
    }
    
    cout << num_solns << endl;
    
}