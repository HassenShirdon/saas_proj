import axios from '@/api/axios'

export const getAccounts = () => {
  return axios.get(`/finance/Accounts/`)
}

export const getAccount = (id) => {
  return axios.get(`/finance/Account/${id}/`)
}

export const createAccount = (account) => {
  return axios.post(`/finance/Accounts/`, account)
}

export const updateAccount = (id, account) => {
  return axios.put(`/finance/Account/${id}/`, account)
}

export const deleteAccount = (id) => {
  return axios.delete(`/finance/Account/${id}/`)
}

// Account Lists
export const getAccountTypes = () => {
  return axios.get(`/finance/AccountLists/`)
}

export const getAccountType = (id) => {
  return axios.get(`/finance/AccountList/${id}/`)
}

export const createAccountTypes = (account) => {
  return axios.post(`/finance/AccountLists/`, account)
}

export const updateAccountType = (id, account) => {
  return axios.put(`/finance/AccountList/${id}/`, account)
}

export const deleteAccountType = (id) => {
  return axios.delete(`/finance/AccountList/${id}/`)
}

// JournalEntries
export const getJournalEntries = () => {
  return axios.get(`/finance/JournalEntries/`)
}

export const getJournalEntry = (id) => {
  return axios.get(`/finance/JournalEntry/${id}/`)
}

export const createJournalEntries = (JournalEntry) => {
  return axios.post(`/finance/JournalEntries/`, JournalEntry)
}

export const updateJournalEntry = (id, JournalEntry) => {
  return axios.put(`/finance/JournalEntries/${id}/`, JournalEntry)
}

export const deleteJournalEntry = (id) => {
  return axios.delete(`/finance/JournalEntry/${id}/`)
}
// JournalEntryLines
export const getJournalEntryLines = () => {
  return axios.get(`/finance/JournalEntryLines/`)
}
export const getJournalEntryLine = (id) => {
  return axios.get(`/finance/JournalEntryLine/${id}/`)
}
export const createJournalEntryLines = (JournalEntryLine) => {
  return axios.post(`/finance/JournalEntryLines/`, JournalEntryLine)
}
export const updateJournalEntryLine = (id, JournalEntryLine) => {
  return axios.put(`/finance/JournalEntryLines/${id}/`, JournalEntryLine)
}
export const deleteJournalEntryLine = (id) => {
  return axios.delete(`/finance/JournalEntryLine/${id}/`)
}

//SupplierInvoices
export const getSupplierInvoices = () => {
  return axios.get(`/finance/SupplierInvoices/`)
}
export const getSupplierInvoice = (id) => {
  return axios.get(`/finance/SupplierInvoice/${id}/`)
}
export const createSupplierInvoices = (SupplierInvoice) => {
  return axios.post(`/finance/SupplierInvoices/`, SupplierInvoice)
}
export const updateSupplierInvoice = (id, SupplierInvoice) => {
  return axios.put(`/finance/SupplierInvoices/${id}/`, SupplierInvoice)
}
export const deleteSupplierInvoice = (id) => {
  return axios.delete(`/finance/SupplierInvoice/${id}/`)
}
// SupplierInvoiceLines
export const getSupplierInvoiceLines = () => {
  return axios.get(`/finance/SupplierInvoiceLines/`)
}
export const getSupplierInvoiceLine = (id) => {
  return axios.get(`/finance/SupplierInvoiceLine/${id}/`)
}
export const createSupplierInvoiceLines = (SupplierInvoiceLine) => {
  return axios.post(`/finance/SupplierInvoiceLines/`, SupplierInvoiceLine)
}
export const updateSupplierInvoiceLine = (id, SupplierInvoiceLine) => {
  return axios.put(`/finance/SupplierInvoiceLines/${id}/`, SupplierInvoiceLine)
}
export const deleteSupplierInvoiceLine = (id) => {
  return axios.delete(`/finance/SupplierInvoiceLine/${id}/`)
}
//supplierPayments
export const getSupplierPayments = () => {
  return axios.get(`/finance/SupplierPayments/`)
}
export const getSupplierPayment = (id) => {
  return axios.get(`/finance/SupplierPayment/${id}/`)
}
export const createSupplierPayments = (SupplierPayment) => {
  return axios.post(`/finance/SupplierPayments/`, SupplierPayment)
}
export const updateSupplierPayment = (id, SupplierPayment) => {
  return axios.put(`/finance/SupplierPayments/${id}/`, SupplierPayment)
}
export const deleteSupplierPayment = (id) => {
  return axios.delete(`/finance/SupplierPayment/${id}/`)
}
//CustomerInvoices
export const getCustomerInvoices = () => {
  return axios.get(`/finance/CustomerInvoices/`)
}
export const getCustomerInvoice = (id) => {
  return axios.get(`/finance/CustomerInvoice/${id}/`)
}
export const createCustomerInvoices = (CustomerInvoice) => {
  return axios.post(`/finance/CustomerInvoices/`, CustomerInvoice)
}
export const updateCustomerInvoice = (id, CustomerInvoice) => {
  return axios.put(`/finance/CustomerInvoices/${id}/`, CustomerInvoice)
}
export const deleteCustomerInvoice = (id) => {
  return axios.delete(`/finance/CustomerInvoice/${id}/`)
}

// CustomerInvoiceLines
export const getCustomerInvoiceLines = () => {
  return axios.get(`/finance/CustomerInvoiceLines/`)
}
export const getCustomerInvoiceLine = (id) => {
  return axios.get(`/finance/CustomerInvoiceLine/${id}/`)
}
export const createCustomerInvoiceLines = (CustomerInvoiceLine) => {
  return axios.post(`/finance/CustomerInvoiceLines/`, CustomerInvoiceLine)
}
export const updateCustomerInvoiceLine = (id, CustomerInvoiceLine) => {
  return axios.put(`/finance/CustomerInvoiceLines/${id}/`, CustomerInvoiceLine)
}
export const deleteCustomerInvoiceLine = (id) => {
  return axios.delete(`/finance/CustomerInvoiceLine/${id}/`)
}

//CustomerPayments
export const getCustomerPayments = () => {
  return axios.get(`/finance/CustomerPayments/`)
}
export const getCustomerPayment = (id) => {
  return axios.get(`/finance/CustomerPayment/${id}/`)
}
export const createCustomerPayments = (CustomerPayment) => {
  return axios.post(`/finance/CustomerPayments/`, CustomerPayment)
}
export const updateCustomerPayment = (id, CustomerPayment) => {
  return axios.put(`/finance/CustomerPayments/${id}/`, CustomerPayment)
}
export const deleteCustomerPayment = (id) => {
  return axios.delete(`/finance/CustomerPayment/${id}/`)
}

// Expenses
export const getExpenses = () => {
  return axios.get(`/finance/Expenses/`)
}
export const getExpense = (id) => {
  return axios.get(`/finance/Expense/${id}/`)
}
export const createExpenses = (Expense) => {
  return axios.post(`/finance/Expenses/`, Expense)
}
export const updateExpense = (id, Expense) => {
  return axios.put(`/finance/Expenses/${id}/`, Expenses)
}
export const deleteExpense = (id) => {
  return axios.delete(`/finance/Expense/${id}/`)
}

//FinancialPeriods
export const getFinancialPeriods = () => {
  return axios.get(`/finance/FinancialPeriods/`)
}

export const getFinancialPeriod = (id) => {
  return axios.get(`/finance/FinancialPeriod/${id}/`)
}
export const createFinancialPeriods = (FinancialPeriod) => {
  return axios.post(`/finance/FinancialPeriods/`, FinancialPeriod)
}
export const updateFinancialPeriods = (id, FinancialPeriod) => {
  return axios.put(`/finance/FinancialPeriods/${id}/`, FinancialPeriod)
}
export const deleteFinancialPeriod = (id) => {
  return axios.delete(`/finance/FinancialPeriod/${id}/`)
}
