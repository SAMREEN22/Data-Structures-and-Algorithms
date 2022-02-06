 public static int interpolationsearch(int[] arr, int x)
 {
        int low = 0;
        int high = arr.length - 1;
        int mid;
        while (arr[low] <=x && arr[high] >=x) 
        {
            if (arr[high] - arr[low] == 0)
                return (low + high)/2;
             mid = low + ((x - arr[low]) * (high - low)) / (arr[high] - arr[low]);  
 
             if (arr[mid] < x)
                 low = mid + 1;
             else if (arr[mid] > x)
                 high = mid - 1;
             else
                 return mid;
        }
        if (arr[low] == x)
            return low;
        else
            return -1; 
 }