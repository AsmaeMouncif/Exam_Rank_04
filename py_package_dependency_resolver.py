def find_key_by_value(p, target_value):
    result = []
    for key, value in p.items():
        if value == target_value:
            result.append(key)
    return result


def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
    result = []
    while packages:
        ready = sorted(find_key_by_value(packages, []))
        if len(ready) == 0:
            return []
        i = 0
        while i < len(ready) :
            key = ready[i]
            result.append(key)
            packages.pop(key)
            for dependencies in packages.values():
                if key in dependencies:
                    dependencies.remove(key)
            i = i + 1
    return result


if __name__ == "__main__":
    # --- subject examples ---
    print(package_dependency_resolver({"app": ["database"], "database": ["driver"], "driver": []}))  # ['driver', 'database', 'app']
    print(package_dependency_resolver({"A": [], "B": ["A"], "C": ["A", "B"]}))  # ['A', 'B', 'C']
    print(package_dependency_resolver({}))  # []
    print(package_dependency_resolver({"X": ["Y"], "Y": ["X"]}))  # []
    print(package_dependency_resolver({"web": [], "api": [], "frontend": ["web"], "backend": ["api"]}))  # ['api', 'web', 'backend', 'frontend']

    # --- edge cases from the subject ---
    print(package_dependency_resolver({"A": ["A"]}))  # []
    print(package_dependency_resolver({"A": ["A"], "B": []}))  # []
    print(package_dependency_resolver({"A": ["Z"]}))  # ['A']
    print(package_dependency_resolver({"A": ["Z"], "B": ["A"]}))  # ['A', 'B']
    print(package_dependency_resolver({"A": ["X", "Y"], "B": ["Z"]}))  # ['A', 'B']
    print(package_dependency_resolver({"A": ["B"], "B": ["C"], "C": ["A"]}))  # []
    print(package_dependency_resolver({"A": ["B"], "B": ["A"], "C": []}))  # []
    print(package_dependency_resolver({"A": [], "B": ["A", "C"], "C": ["B"]}))  # []

    # --- robustness ---
    print(package_dependency_resolver({"A": [], "B": ["A", "A"]}))  # ['A', 'B']
    print(package_dependency_resolver({"A": []}))  # ['A']
    print(package_dependency_resolver({"c": [], "a": [], "b": []}))  # ['a', 'b', 'c']
    print(package_dependency_resolver({"C": ["B"], "B": ["A"], "A": []}))  # ['A', 'B', 'C']
    print(package_dependency_resolver({"z": [], "m": [], "a": [], "top": ["z", "m", "a"]}))  # ['a', 'm', 'z', 'top']
    print(package_dependency_resolver({"api": [], "web": [], "backend": ["api"], "frontend": ["web"]}))  # ['api', 'web', 'backend', 'frontend']