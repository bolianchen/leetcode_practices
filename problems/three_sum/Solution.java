/* 
 * Use the libraries provided by the textbook of Princeton Algorithms for Testing
 * https://algs4.cs.princeton.edu/code/ 
 */
import edu.princeton.cs.algs4.*;
import java.util.*;

public class Solution {

    public static List<List<Integer>> threeSum(int[] nums) {

        List<List<Integer>> output = new ArrayList<>();

        // sort nums
        Arrays.sort(nums);

        // build a lookup map for all the entries in nums
        // to search the entry complementing to each two sum
        Map<Integer, Integer> map = new HashMap<>();

        int idx = 0;

        // only put the largest num to the lookup map
        for (int num: nums) {
            map.put(num, idx);
            idx += 1;
        }

        // maintain a set of Lists to prevent duplicates
        Set<List<Integer>> seenLists = new HashSet<>();

        for (int i = 0; i<nums.length; i++) {
            for (int j = i+1; j<nums.length; j++) {
                if (map.containsKey(-nums[i]-nums[j])) {
                    int k = map.get(-nums[i]-nums[j]);
                    if (k > j) {
                        List<Integer> saveList = new ArrayList<>();
                        saveList.add(nums[i]);
                        saveList.add(nums[j]);
                        saveList.add(-nums[i]-nums[j]);
                        Collections.sort(saveList);
                        if (!seenLists.contains(saveList)) {
                            seenLists.add(saveList);
                            output.add(saveList);
                        }
                    }
                }
            }
        }

        return output;
    }

    public static void main(String[] args) {
        In in = new In(args[0]);
        int[] nums = in.readAllInts();
        List<List<Integer>> output = threeSum(nums);
    }
}
