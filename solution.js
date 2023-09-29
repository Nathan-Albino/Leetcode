
const containsDuplicate = function (nums) {
  let testObj = {}

  for (let i = 0; i < nums.length; i++) {
    if (testObj[nums[i]]) {
      return true
    } else {
      testObj[nums[i]] = true
    }
  }

  return false
}

const isAnagram = function (s, t) {
  const map = new Map()

  if (s.length != t.length) {
    return false
  }

  for (let i = 0; i < s.length; i++) {
    if (map.has(s[i])) {
      map.set(s[i], map.get(s[i]) + 1)
    } else {
      map.set(s[i], 1)
    }
  }

  for (let i = 0; i < t.length; i++) {
    if (!map.has(t[i])) {
      return false
    }

    map.set(t[i], map.get(t[i]) - 1)
  }

  for (const value of map.values()) {
    if (value != 0) {
      return false
    }
  }

  return true
}

const twoSum = (nums, target) => {
  const map = new Map()

  for (let i = 0; i < nums.length; i++) {
    result = target - nums[i]

    if (map.get(result) != null) {
      return [map.get(result), i]
    } else {
      map.set(nums[i], i)
    }
  }
}
