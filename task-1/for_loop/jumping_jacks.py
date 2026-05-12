total = 100
done = 0

while done < total:
    done += 10
    print(f"You completed {done} jumping jacks")

    if done == total:
        print("Congratulations! You completed the workout")
        break

    tired = input("Are you tired? (yes/y or no/n): ").lower()

    if tired in ("yes", "y"):
        skip = input("Do you want to skip the remaining sets? (yes/y or no/n): ").lower()

        if skip in ("yes", "y"):
            print(f"You completed a total of {done} jumping jacks")
            break
        else:
            remaining = total - done
            print(f"{remaining} jumping jacks remaining")

    elif tired in ("no", "n"):
        remaining = total - done
        print(f"{remaining} jumping jacks remaining")
