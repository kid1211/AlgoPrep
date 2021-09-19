convertedS.replacingOccurrences(of: "#", with: "")

for char in s {
    convertedS += [char]
    convertedS += ["#"]
}

convertedS.replacingOccurrences(of: "#", with: "")

func getIndex(_ i: Int) -> String.Index {
    return s.index(s.startIndex, offsetBy: i)
}