class Solution {
public:
    vector<int> prefix;
    vector<vector<int>> dp;

    int dfs(int i, int j, vector<int>& stoneValue) {
        if (i == j)
            return 0;

        if (dp[i][j] != -1)
            return dp[i][j];

        int maxx = 0;

        for (int k = i; k < j; k++) {
            int left = prefix[k + 1] - prefix[i];
            int right = prefix[j + 1] - prefix[k + 1];

            int ali;

            if (left > right) {
                ali = right + dfs(k + 1, j, stoneValue);
            } else if (right > left) {
                ali = left + dfs(i, k, stoneValue);
            } else {
                ali = max(
                    left + dfs(i, k, stoneValue),
                    right + dfs(k + 1, j, stoneValue)
                );
            }

            maxx = max(maxx, ali);
        }

        return dp[i][j] = maxx;
    }

    int stoneGameV(vector<int>& stoneValue) {
        int n = stoneValue.size();

        prefix.resize(n + 1, 0);

        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + stoneValue[i];
        }

        dp.assign(n, vector<int>(n, -1));

        return dfs(0, n - 1, stoneValue);
    }
};