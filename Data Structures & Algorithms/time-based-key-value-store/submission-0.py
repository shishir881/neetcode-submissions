class TimeMap:

    def __init__(self):
        self.stamp={}  

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.stamp:
            self.stamp[key].append([timestamp,value])
        else:
            self.stamp[key]=[[timestamp,value]] 

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.stamp or timestamp<self.stamp[key][0][0]:
            return ""

        else:
            values = self.stamp[key]
            l=0
            r=len(values)-1
            res=""
            while l<=r:
                mid=(l+r)//2
                if values[mid][0]==timestamp:
                    return values[mid][1]
                elif values[mid][0]<timestamp:
                    res=values[mid][1]
                    l=mid+1
                else:
                    r=mid-1
            return res

        
