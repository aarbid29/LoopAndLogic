class Solution:
    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
        contain = set(supplies)
        adj = defaultdict(list)
        visited = set()
        memo = {}

        for i, recipe in enumerate(recipes): 
            adj[recipe].extend(ingredients[i])

        def check(recipe):

            if recipe in visited:
                return False
            if recipe in memo:
                return memo[recipe]
            visited.add(recipe)


            for ingredient in adj[recipe]:
                if ingredient in contain:
                    continue
                    
                if ingredient not in adj:
                    visited.remove(recipe)
                    memo[recipe] = False
                    return False

                if not check(ingredient):
                    visited.remove(recipe)
                    memo[recipe]=False
                    return False
            visited.remove(recipe)
            contain.add(recipe)
            memo[recipe]=True
            return True

 
        res = []
        for recipe in recipes:
            if check(recipe):
                res.append(recipe)

        return res 


        

        