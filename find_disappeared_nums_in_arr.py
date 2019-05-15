class Sol:
    def find_disappeared_nums_in_arr(self,arr):
        m=max(arr)
        l=[]
        for i in range(1,m+1):
            l.append(i)
        return list(set(l)-set(arr))

if __name__ == '__main__':
    p1=Sol()
    print(p1.find_disappeared_nums_in_arr([1,2,3,4,3,6,8,8]))
