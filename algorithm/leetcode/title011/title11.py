class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        m = {}
        l = []
        for i, v in enumerate(height):
            l.append(v)
            if v in m:
                m[v][0] = min(m[v][0], i)
                m[v][1] = max(m[v][1], i)
            else:
                m[v] = [ i, i ]
        l.sort(reverse=True)
        mx = 0
        for i, v in enumerate(l):
            mx = max(mx, v * ( m[v][1] -  m[v][0]))
            if i == len(l) - 1:
                pass
            elif len(height) * l[i + 1] <= mx:
                return mx
            else:
                vv = l[i + 1]
                m[vv][0] = min(m[vv][0], m[v][0])
                m[vv][1] = max(m[vv][1], m[v][1])
        return mx