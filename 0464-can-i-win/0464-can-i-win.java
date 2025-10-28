class Solution {
    private Map<Integer, Boolean> memo = new HashMap<>();
    private int max;
    
    public boolean canIWin(int maxChoosableInteger, int desiredTotal) {
        max = maxChoosableInteger;
        
        int sum = (max * (max + 1)) / 2;
        if (sum < desiredTotal) return false;
        
        if (desiredTotal <= 0) return true;
        
        return dfs(0, desiredTotal);
    }
    
    private boolean dfs(int usedMask, int remaining) {
        if (memo.containsKey(usedMask)) return memo.get(usedMask);
        
        for (int i = 1; i <= max; i++) {
            int bit = 1 << (i - 1);
            if ((usedMask & bit) != 0) continue;
            
            if (i >= remaining || !dfs(usedMask | bit, remaining - i)) {
                memo.put(usedMask, true);
                return true;
            }
        }
        
        memo.put(usedMask, false);
        return false;
    }
}
