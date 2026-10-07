def find_key_by_value(p, target_value):
    result = []
    for key, value in p.items():
        if value == target_value:
            result.append(key)
    return result


def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
    new_dict = {}
    for key, value in packages.items():
        new_dict[key] = []
        for v in value:
            if v in packages and v not in new_dict[key]:
                new_dict[key].append(v)
    result = []
    while new_dict:
        ready = sorted(find_key_by_value(new_dict, []))
        if len(ready) == 0:
            return []
        i = 0
        while i < len(ready):
            key = ready[i]
            result.append(key)
            new_dict.pop(key)
            for dependencies in new_dict.values():
                if key in dependencies:
                    dependencies.remove(key)
            i = i + 1
    return result

if __name__ == "__main__":
    print(package_dependency_resolver({"app": ["database"], "database": ["driver"], "driver": []}))
    print(package_dependency_resolver({"A": [], "B": ["A"], "C": ["A", "B"]}))
    print(package_dependency_resolver({}))
    print(package_dependency_resolver({"X": ["Y"], "Y": ["X"]}))
    print(package_dependency_resolver({"web": [], "api": [], "frontend": ["web"], "backend": ["api"]}))
