# def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
#     result = []
#     installed = set()
#     remaining = set(packages)

#     while remaining:
#         ready = []

#         for package in remaining:
#             can_install = True

#             for dependency in packages[package]:
#                 if dependency in packages and dependency not in installed:
#                     can_install = False
#                     break

#             if can_install:
#                 ready.append(package)

#         if not ready:
#             return []

#         ready.sort()

#         for package in ready:
#             result.append(package)
#             installed.add(package)
#             remaining.remove(package)

#     return result


def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
	result = []
	install = set()
	remainding = set(packages)

	while remainding:
		ready = []
		for package in remainding:
			can_install = True
			for dependency in packages[package]:
				if dependency in package and dependency not in install:
					can_install = False
					break
			if can_install:
				ready.append(package)
		if not ready:
			return []
		ready.sort()

		for package in ready:
			result.append(package)
			install.add(package)
			remainding.remove(package)

	return result

print(package_dependency_resolver({"web": [], "api": [], "frontend": ["web"], "backend": ["api"]}))