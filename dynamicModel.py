class DynamicModel:
    nodes = []
    pathCost = []
    pListStartFromA = []
    strategyVector = []

    # 问题的关键是如何规划数据文件的表达形式---
    # 处理单一起点
    def initModel(self, dataLines):
        # 首先识别全部的阶段--全部的字母 = 阶段数+1
        m = len(dataLines) + 1
        zimu = []
        for i in range(0, m):
            zimu.append(chr(ord('A') + i))
        print("全部字母：", zimu)

        # 识别节点、以及边
        self.nodes.append(['A'])  # 先增加起始节点
        for i in range(len(dataLines)):
            vtemp = dataLines[i].split(";")
            vvtemp = vtemp[0].split()
            nv = len(vvtemp)
            v = []  # 分析每一行的节点
            for j in range(0, nv):
                if nv > 1:
                    v.append("%c%d" % (zimu[i + 1], j + 1))
                else:
                    v.append(zimu[i + 1])
            self.nodes.append(v)

            #
            ne = len(vtemp)
            ev = []
            for j in range(0, ne):
                vvtemp = vtemp[j].split()
                nne = len(vvtemp)
                eev = []
                for k in range(nne):
                    eev.append(int(vvtemp[k]))
                ev.append(eev)
            self.pathCost.append(ev)

        print(self.nodes)
        print(self.pathCost)
        return

    def optimization(self):
        print("\n动态规划分析：")
        print(self.nodes)
        m = len(self.nodes) - 1
        print("可以划分成%d个阶段。\n" % m)

        # 对阶段进行循环
        for i in range(m):
            print("\n阶段分析：", self.nodes[i], "--->", self.nodes[i + 1])
            print("状态，阶段的起点", self.nodes[i])
            statusNumber = len(self.nodes[i])
            print("%d 阶段，共有%d个状态" % (i, statusNumber))
            # 可选决策是当前状态的，可能的终点
            selectNumber = len(self.nodes[i + 1])
            print("%d 阶段，可选决策：%d" % (i, selectNumber), self.nodes[i + 1])

            ss = []
            # 决策循环在外面
            for j in range(0, selectNumber):
                # 对每个状态进行循环
                distance = []
                uu = []
                d = {}
                for k in range(statusNumber):
                    # 路径计算
                    tmpu = {}
                    tmpu['i'] = self.nodes[i][k]  # 起点
                    tmpu['j'] = self.nodes[i + 1][j]  # 终点
                    uu.append(tmpu)
                    # 计算长度
                    # 这一句是关键了
                    eLen = self.pathCost[i][k][j]
                    if (i == 0):
                        distance.append(eLen)
                    else:
                        distance.append(self.strategyVector[i - 1][k]['distance'] + eLen)

                # 记录决策---这里缺少--寻优
                print("寻优：", distance)
                # 寻优
                opt = min(distance)
                optk = distance.index(opt)
                d['i'] = uu[optk]['i']
                d['j'] = uu[optk]['j']
                d['distance'] = opt
                d['u'] = uu[optk]
                d['uk'] = optk
                ss.append(d)
                print("%d 阶段 %d状态 决策结果：" % (i, j), opt, uu[optk])
                print(uu)
            # 阶段循环完成后，添加进决策列表
            self.strategyVector.append(ss)

        #print("\n", self.strategyVector)
        print("优化结果：")
        for v in self.strategyVector:
            print(v)
        return

    def displayResult(self):
        print("\n\n最后的最优策略：")
        m = len(self.strategyVector)
        uu = ['G']
        i = m - 1
        j = 0
        while (i >= 0):
            # print(self.strategyVector[i])
            uu.append(self.strategyVector[i][j]['i'])
            i = i - 1
            j = self.strategyVector[i][j]['uk']
        # print(uu)
        uu.reverse()
        print(uu, "最短距离是：", self.strategyVector[m - 1][0]['distance'])
        return
