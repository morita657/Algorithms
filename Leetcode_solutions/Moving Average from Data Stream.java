import java.util.ArrayList;
import java.util.List;

class MovingAverage {
    int size;
    List queue = new ArrayList<Integer>();

    /** Initialize your data structure here. */
    public MovingAverage(int size) {
        this.size = size;
    }

    public double next(int val) {
        queue.add(val);
        int windowSum = 0;
        for (int i = Math.max(0, queue.size() - size); i < queue.size(); ++i) {
            windowSum += (int) queue.get(i);
        }
        return windowSum * 1.0 / Math.min(queue.size(), size);
    }
}
