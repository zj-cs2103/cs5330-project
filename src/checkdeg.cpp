#include <bits/stdc++.h>
using namespace std;

int num_clauses, num_vars;
vector<vector<int> > clauses;
vector<int> deg;

int main() {
    
    string xxx;
    cin >> xxx >> xxx >> num_vars >> num_clauses;
    
    for (int i = 0; i < num_clauses; i++) {
        vector<int> clause;
        deg.push_back(0);
        int var;
        while (cin >> var) {
            if (var == 0) break;
            clause.push_back(abs(var));
        }
        clauses.push_back(clause);
    }
    
    for (int i = 0; i < clauses.size(); i++) {
        for (int j = 0; j < clauses.size(); j++) {
            if (i == j) continue;
            bool dep = false;
            for (int k = 0; k < clauses[i].size(); k++) {
                if (find(clauses[j].begin(), clauses[j].end(), clauses[i][k]) != clauses[j].end()) {
                    dep = true;
                    break;
                }
            }
            if (dep) {
                deg[i]++;
            }
        }
    }
    
    // for (int i = 0; i < clauses.size(); i++) {
    //     cout << deg[i] << " ";
    // }
    // cout << endl;
    
    cout << *max_element(deg.begin(), deg.end()) << " ";
}