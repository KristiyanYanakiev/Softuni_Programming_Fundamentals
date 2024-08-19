version = input().split(".")
version_as_int = int("".join(version))

updated_version = version_as_int + 1

final_version = ".".join(str(updated_version))

print(final_version)