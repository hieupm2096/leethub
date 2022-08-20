class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        baseColor = image[sr][sc]
        if color != baseColor:
            self.dfs(image, m, n, sr, sc, color, baseColor)
        return image
            
    def dfs(self, image: List[List[int]], m: int, n: int, sr: int, sc: int, color: int, baseColor: int):
        if sr < 0 or sr >= m or sc < 0 or sc >= n or image[sr][sc] != baseColor:
            return
        image[sr][sc] = color
        
        self.dfs(image, m, n, sr - 1, sc, color, baseColor)
        self.dfs(image, m, n, sr + 1, sc, color, baseColor)
        self.dfs(image, m, n, sr, sc - 1, color, baseColor)
        self.dfs(image, m, n, sr, sc + 1, color, baseColor)
            