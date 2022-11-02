def mergesort_topdown(inp_arr):
    # Ends the recursion if arr is size 1
    if len(inp_arr) > 1:
        # Find the middle of the input array, abs
        middle = len(inp_arr) // 2

        # Slice array down the middle
        left_arr = inp_arr[:middle]
        right_arr = inp_arr[middle:]

        # Recurse on the left and right slices created, til we hit size 1 array and stop
        mergesort_topdown(left_arr)
        mergesort_topdown(right_arr)

        # Iterators
        p = 0
        q = 0
        r = 0

        # While iterator 1 and 2 are less than the size of the left and right arrays respectively
        while p < len(left_arr) and q < len(right_arr):
            # If the left_arr at iterator 1 is less than right_arr at iterator 2
            if left_arr[p] < right_arr[q]:
                # Assign left_arr at iter 1 to the inp_arr at iter 3
                inp_arr[r] = left_arr[p]
                # Increment iter 1 and loop
                p += 1
            else:
                # Assign right_arr at iter 2 to the inp_arr at iter 3
                inp_arr[r] = right_arr[q]
                # Increment iter 2 and loop
                q += 1

            # Increment iter 3 at end of while and loop
            r += 1

        # append any remaining from left_arr
        while p < len(left_arr):
            inp_arr[r] = left_arr[p]
            p += 1
            r += 1

        # append any remaining from the right_arr
        while q < len(right_arr):
            inp_arr[r] = right_arr[q]
            q += 1
            r += 1
