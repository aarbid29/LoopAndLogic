class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:

        dictt = set(bank)
        dq = deque()
        dq.append(startGene)
        lvl = 0 

        gene_made = {startGene}
        while dq :
            size = len(dq)
            changed = False

            for _ in range(size):
                word = dq.popleft()

                if word == endGene:
                    return lvl
                
                for i in range(len(word)):
                    for char in "ACGT":
                        new_gene = word[:i]+ char + word[i+1:]

                        if new_gene in dictt and new_gene not in gene_made:
                            changed = True
                            gene_made.add(new_gene)
                            dq.append(new_gene)
            
            if changed:
                lvl+=1
        return -1
        