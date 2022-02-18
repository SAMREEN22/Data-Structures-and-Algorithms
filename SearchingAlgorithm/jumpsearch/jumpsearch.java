public static int jumpSearch(int[] arr, int element)
    {
        int n = arr.length;
        int step = (int)Math.floor(Math.sqrt(n));
        int prev = 0;
        while (arr[Math.min(step, n)-1] < element)
        {
            prev = step;
            step += (int)Math.floor(Math.sqrt(n));
            if (prev>=n)
                return -1;
        }
        while (arr[prev]<element)
        {
            prev++;
            if (prev==Math.min(step, n))
                return -1;
        }
        if (arr[prev]==element)
            return prev;
            
        return -1;
    }