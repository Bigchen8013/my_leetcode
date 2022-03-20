'''
题目描述;
有一幅以 m x n 的二维整数数组表示的图画 image ，其中 image[i][j] 表示该图画的像素值大小。

你也被给予三个整数 sr ,  sc 和 newColor 。你应该从像素 image[sr][sc] 开始对图像进行 上色填充 。

为了完成 上色工作 ，从初始像素开始，记录初始坐标的 上下左右四个方向上 像素值与初始坐标相同的相连像素点，接着再记录这四个方向上符合条件的像素点与他们对应 四个方向上 像素值与初始坐标相同的相连像素点，……，重复该过程。将所有有记录的像素点的颜色值改为 newColor 。

最后返回 经过上色渲染后的图像 。

 来自：https://leetcode-cn.com/problems/flood-fill/solution/python3-dfs-yu-bfs-liang-chong-fang-fa-san-chong-s/

'''

from typing import List
from queue import Queue
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # 起始颜色和目标颜色需要不一致，否则会导致死循环
        if image[sr][sc] == newColor:
            return image
        
        # 设置四个方向的偏移量
        directions = {(1,0),(-1,0),(0,1),(0,-1)}
        # 构造一个队列
        que = Queue()
        # 将初始的点添加进去
        que.put((sr,sc))
        # 记录目标初始颜色
        origin_color = image[sr][sc]
        # 当队列不为空
        while not que.empty():
            # 去除队列的点并染色
            point = que.get()
            image[point[0]][point[1]] = newColor
            # 遍历四个方向
            for direction in directions:
                # 新的点
                new_sr = point[0] + direction[0]
                new_sc = point[1] + direction[1]
                # 如果该点在定义的区域内且它和原来的颜色相同(并不是目标颜色)，则加进队列中
                if 0 <= new_sr < len(image) and 0 <= new_sc < len(image[0]) and image[new_sr][new_sc] == origin_color:
                    que.put((new_sr,new_sc))
        return image

     # 方法二
    def floodFill1(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
         if newColor == image[sr][sc]:
             return image
        
         que, origin_color = [(sr,sc)], image[sr][sc]
         while que:
             point = que.pop()
             image[point[0]][point[1]] = newColor
            #  (point[0],point[1]+1),(point[0],point[1]-1),(point[0]+1,point[1]),(point[0]-1,point[1])
             for new_sr, new_sc in zip((point[0],point[0],point[0]+1,point[0]-1),(point[1]+1,point[1]-1,point[1],point[1])):
                 if 0 <= new_sr < len(image) and 0 <= new_sc < len(image[0]) and image[new_sr][new_sc] == origin_color:
                     que.insert(0, (new_sr,new_sc))
         return image
         

if __name__:
    s = Solution()
    # -----------------------------------
    # image = [[1,1,1],[1,1,0],[1,0,1]]
    # sr = 1
    # sc = 1
    # newColor = 2
    # ----------------------------
    image = [[0,0,0],[0,0,0]]
    sr = 0
    sc = 0
    newColor = 2
    result = s.floodFill(image, sr, sc, newColor)
    print("result:",result)
    result1 = s.floodFill1(image, sr, sc, newColor)
    print("result1:",result1)
