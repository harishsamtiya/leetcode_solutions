class Solution {
public:
    int n, m;
    void four_dirn(vector<vector<char>>& grid, int i, int j){
        if (i>=0 && i<n && j>=0 && j<m && grid[i][j] == '1'){
            grid[i][j] = '2';
            four_dirn(grid, i, j+1);
            four_dirn(grid, i+1, j);
            four_dirn(grid, i, j-1);
            four_dirn(grid, i-1, j);
        }
    }
    int numIslands(vector<vector<char>>& grid) {
        n = grid.size();
        m = grid[0].size();
        int island_count = 0;
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                if (grid[i][j] == '1'){
                    island_count++;
                    four_dirn(grid, i, j);
                }
                
            }
        }
        return island_count;
    }
};