class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        base_point1 = coordinates[0]
        base_x1 = base_point1[0]
        base_y1 = base_point1[1]
        
        base_point2 = coordinates[1]
        base_x2 = base_point2[0]
        base_y2 = base_point2[1]
        
        if base_x2 == base_x1:
            ref_slope = f'vertical line at {base_x2}'
            
        elif base_y2 == base_y1:
            ref_slope = f'horizontal line at {base_y2}'
            
        else:
            ref_slope = (base_y2 - base_y1) / (base_x2 - base_x1)
            
        for point in coordinates[2:]:
            
            if point[0] == base_x1:
                slope = f'vertical line at {point[0]}'
            
            elif point[1] == base_y1:
                slope = f'horizontal line at {point[1]}'
                
            else:
                slope = (point[1]-base_y1) / (point[0]-base_x1)
                
            if slope != ref_slope:
                return False
            
        return True
