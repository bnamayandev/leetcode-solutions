func hasDuplicate(nums []int) bool {
    has := make(map[int]bool)

    for _, n := range nums {
        if has[n]  {
            return true
        } else {
            has[n] = true
        }
    } 
    return false
}
