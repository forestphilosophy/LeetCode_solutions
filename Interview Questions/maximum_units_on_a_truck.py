class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: x[1], reverse=True)

        remaining = truckSize
        maximum = 0
        
        for box in boxTypes:
            num_of_boxes = box[0]

            if num_of_boxes < remaining:
                
                maximum += num_of_boxes * box[1]
                remaining -= num_of_boxes
                
            elif num_of_boxes > remaining:
                
                maximum += remaining * box[1]
                return maximum
            
            elif num_of_boxes == remaining:
                maximum += num_of_boxes * box[1]
                remaining -= num_of_boxes
                
                return maximum
            
        return maximum
