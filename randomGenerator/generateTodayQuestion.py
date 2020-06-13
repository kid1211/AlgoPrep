def main():
    with open("randomGenerator/PROBLEMS.md") as file:  # Use file to refer to the file object
        data = file.read()

    with open('Today.md', 'w') as file:  # Use file to refer to the file object
        file.write(data)


if __name__ == "__main__":
    # execute only if run as a script
    main()
