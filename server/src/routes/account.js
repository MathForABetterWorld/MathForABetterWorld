// Here the routes will be listed with correspodning middleware

// Example routes from another app:
/**
 * router.post(
  "/signup",
  body("email", "Email is required").isEmail(),
  body("name", "Name is required").notEmpty(),
  body("phoneNumber").optional().isMobilePhone(),
  validator.isUniqueEmail,
  validator.isUniquePhone,
  controller.create
);

router.post(
  "/login",
  body("email", "Email is required").isEmail(),
  validator.emailExists,
  controller.login
);
 */
