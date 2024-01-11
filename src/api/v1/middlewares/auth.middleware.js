import User from "../models/user.js";
export const authenticatePassword = async (req, res, next) => {
  //   create user
  //   const userData = { username: "Ehsan", password: "2094" };
  //   const user = new User(userData);
  //   await user.save();

  try {
    const { username, password } = req.body;
    const user = await User.findOne({ username });

    if (!user) {
      return res.status(401).json({ message: "Invalid credentials" });
    }

    if (user.password !== password) {
      return res.status(401).json({ message: "Invalid credentials" });
    }
  } catch (error) {
    console.error("Login error:", error);
    return res.status(500).json({ message: "Internal server error" });
  }

  next();
};
