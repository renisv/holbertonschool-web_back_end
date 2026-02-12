function getCurrentYear() {
<<<<<<< HEAD
  const date = new Date();
  return date.getFullYear();
}

export default function getBudgetForCurrentYear(income, gdp, capita) {
  const budget = {
    [`income-${getCurrentYear()}`]: income,
    [`gdp-${getCurrentYear()}`]: gdp,
    [`capita-${getCurrentYear()}`]: capita,
  };

  return budget;
=======
    const date = new Date();
    return date.getFullYear();
}

export default function getBudgetForCurrentYear(income, gdp, capita) {
    const budget = {
        [`income-${getCurrentYear()}`]: income,
        [`gdp-${getCurrentYear()}`]: gdp,
        [`capita-${getCurrentYear()}`]: capita,
    };

    return budget;
>>>>>>> upstream/main
}
