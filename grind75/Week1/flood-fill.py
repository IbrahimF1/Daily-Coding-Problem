# https://leetcode.com/problems/flood-fill

class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """

        if image[sr][sc] == color:
            return image
        
        self.filler(image, sr, sc, color, image[sr][sc])
        return image
        

    def filler(self, image, sr, sc, color, oldColor):
        print(len(image))
        print(len(image[0]))
        if (sr < 0 or sr > len(image)-1) or (sc < 0 or sc > len(image[0])-1) or image[sr][sc] != oldColor:
            return

        image[sr][sc] = color

        self.filler(image, sr+1, sc, color, oldColor)
        self.filler(image, sr-1, sc, color, oldColor)
        self.filler(image, sr, sc+1, color, oldColor)
        self.filler(image, sr, sc-1, color, oldColor)
