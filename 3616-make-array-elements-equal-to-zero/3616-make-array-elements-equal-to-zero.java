class Solution {
    public int countValidSelections(int[] nums) {
        int n = nums.length;
        int validCount = 0;

        for (int start = 0; start < n; start++) {
            if (nums[start] != 0) continue;

            for (int dir : new int[]{-1, 1}) {
                int curr = start;
                int d = dir;
                boolean success = true;
                int[] backup = nums.clone();

                while (curr >= 0 && curr < n) {
                    if (nums[curr] == 0) {
                        curr += d;
                    } else {
                        nums[curr]--;
                        d = -d;
                        curr += d;
                    }
                }

                for (int v : nums) {
                    if (v != 0) {
                        success = false;
                        break;
                    }
                }

                if (success) validCount++;

                System.arraycopy(backup, 0, nums, 0, n);
            }
        }
        return validCount;
    }
}