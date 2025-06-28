<template>
    <div class="container-fluid p-2">
        <div class="d-flex justify-content-between align-items-center mb-4">
            <h1 class="h2 mb-0">Expenses</h1>
            <button @click="addNewExpense" class="btn btn-primary" type="button">
                <i class="fas fa-plus me-2"></i>Add Expense
            </button>
        </div>
        <!-- loading State -->
        <div v-if="store.loading" class="text-center py-5">
            <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
            <p class="mt-2 text-muted">Loading expenses...</p>
        </div>

        <div v-else class="table-responsive">
            <table class="table table-striped table-bordered">
                <thead class="table-dark">
                    <tr>
                        <th>S. No</th>
                        <th>expense_date</th>
                        <th>Amount</th>
                        <th>Description</th>
                        <th>Expense Number</th>
                        <th>Vendor</th>
                        <th>Tax Amount</th>
                        <th>Expense Account</th>
                        <th>Payment Method</th>
                        <th>Journal Entry</th>
                        <th>Notes</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(expense, index) in displayExpense" :key="expense.id || `new-${index}`"
                        :class="{ 'table-warning': expense.isEditing || expense.isNew }">
                        <th scope="row">{{ expense.isNew ? 'NEW' : index + 1 }}</th>

                        <!-- Expense Date Field -->
                        <td>
                            <input v-if="expense.isEditing || expense.isNew" v-model="expense.expense_date" type="date"
                                class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.expense_date`] }" placeholder="Expense Date"
                                @blur="validateField('expense_date', index)" />
                            <div v-if="errors[`${index}.expense_date`]" class="invalid-feedback">
                                {{ errors[`${index}.expense_date`] }}
                            </div>
                            <span v-if="!(expense.isEditing || expense.isNew)" class="fw-semibold">{{
                                expense.expense_date }}</span>
                        </td>

                        <!-- Amount Field -->
                        <td class="text-truncate">
                            <input v-if="expense.isEditing || expense.isNew" type="number" v-model="expense.amount"
                                class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.amount`] }" placeholder="Amount"
                                @blur="validateField('amount', index)" />
                            <div v-if="errors[`${index}.amount`]" class="invalid-feedback">
                                {{ errors[`${index}.amount`] }}
                            </div>
                            <span v-if="!(expense.isEditing || expense.isNew)" class="fw-semibold">{{ expense.amount
                                }}</span>
                        </td>

                        <!-- Description Field -->
                        <td class="text-truncate">
                            <input v-if="expense.isEditing || expense.isNew" type="text" v-model="expense.description"
                                class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.description`] }" placeholder="Description"
                                @blur="validateField('description', index)" />
                            <div v-if="errors[`${index}.description`]" class="invalid-feedback">
                                {{ errors[`${index}.description`] }}
                            </div>
                            <span v-if="!(expense.isEditing || expense.isNew)" class="fw-semibold">{{
                                expense.description }}</span>
                        </td>

                        <!-- Expense Number Field -->
                        <td class="text-truncate">
                            <input v-if="expense.isEditing || expense.isNew" type="text"
                                v-model="expense.expense_number" class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.expense_number`] }"
                                placeholder="Expense Number" @blur="validateField('expense_number', index)" />
                            <div v-if="errors[`${index}.expense_number`]" class="invalid-feedback">
                                {{ errors[`${index}.expense_number`] }}
                            </div>
                            <span v-if="!(expense.isEditing || expense.isNew)" class="fw-semibold">{{
                                expense.expense_number }}</span>
                        </td>

                        <!-- Vendor Field -->
                        <td class="text-truncate">
                            <input v-if="expense.isEditing || expense.isNew" type="text" v-model="expense.vendor"
                                class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.vendor`] }" placeholder="Vendor"
                                @blur="validateField('vendor', index)" />
                            <div v-if="errors[`${index}.vendor`]" class="invalid-feedback">
                                {{ errors[`${index}.vendor`] }}
                            </div>
                            <span v-if="!(expense.isEditing || expense.isNew)" class="fw-semibold">{{ expense.vendor
                                }}</span>
                        </td>

                        <!-- Tax Amount Field -->
                        <td class="text-truncate">
                            <input v-if="expense.isEditing || expense.isNew" type="number" v-model="expense.tax_amount"
                                class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.tax_amount`] }" placeholder="Tax Amount"
                                @blur="validateField('tax_amount', index)" />
                            <div v-if="errors[`${index}.tax_amount`]" class="invalid-feedback">
                                {{ errors[`${index}.tax_amount`] }}
                            </div>
                            <span v-if="!(expense.isEditing || expense.isNew)" class="fw-semibold">{{ expense.tax_amount
                                }}</span>
                        </td>

                        <!-- Expense Account Field -->
                        <td class="text-truncate">
                            <input v-if="expense.isEditing || expense.isNew" type="text"
                                v-model="expense.expense_account" class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.expense_account`] }"
                                placeholder="Expense Account" @blur="validateField('expense_account', index)" />
                            <div v-if="errors[`${index}.expense_account`]" class="invalid-feedback">
                                {{ errors[`${index}.expense_account`] }}
                            </div>
                            <span v-if="!(expense.isEditing || expense.isNew)" class="fw-semibold">{{
                                expense.expense_account }}</span>
                        </td>

                        <!-- Payment Method Field -->
                        <td class="text-truncate">
                            <input v-if="expense.isEditing || expense.isNew" type="text"
                                v-model="expense.payment_method" class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.payment_method`] }"
                                placeholder="Payment Method" @blur="validateField('payment_method', index)" />
                            <div v-if="errors[`${index}.payment_method`]" class="invalid-feedback">
                                {{ errors[`${index}.payment_method`] }}
                            </div>
                            <span v-if="!(expense.isEditing || expense.isNew)" class="fw-semibold">{{
                                expense.payment_method }}</span>
                        </td>

                        <!-- Journal Entry Field -->
                        <td class="text-truncate">
                            <input v-if="expense.isEditing || expense.isNew" type="text" v-model="expense.journal_entry"
                                class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.journal_entry`] }" placeholder="Journal Entry"
                                @blur="validateField('journal_entry', index)" />
                            <div v-if="errors[`${index}.journal_entry`]" class="invalid-feedback">
                                {{ errors[`${index}.journal_entry`] }}
                            </div>
                            <span v-if="!(expense.isEditing || expense.isNew)" class="fw-semibold">{{
                                expense.journal_entry }}</span>
                        </td>

                        <!-- Notes Field -->
                        <td class="text-truncate">
                            <textarea v-if="expense.isEditing || expense.isNew" v-model="expense.notes"
                                class="form-control form-control-sm" :class="{ 'is-invalid': errors[`${index}.notes`] }"
                                placeholder="Notes" @blur="validateField('notes', index)"></textarea>
                            <div v-if="errors[`${index}.notes`]" class="invalid-feedback">
                                {{ errors[`${index}.notes`] }}
                            </div>
                            <span v-if="!(expense.isEditing || expense.isNew)" class="fw-semibold">{{ expense.notes
                                }}</span>
                        </td>
                        <td>
                            <div class="btn-group" role="group">
                                <button v-if="expense.isEditing || expense.isNew" @click="handleSave(index)"
                                    class="btn btn-success btn-sm" type="button">
                                    <i class="fas fa-save"></i> Save
                                </button>
                                <button v-else @click="editExpense(index)" class="btn btn-warning btn-sm" type="button">
                                    <i class="fas fa-edit"></i> Edit
                                </button>
                                <button v-if="!expense.isNew" @click="deleteExpense(index)"
                                    class="btn btn-danger btn-sm" type="button">
                                    <i class="fas fa-trash"></i> Delete
                                </button>
                                <button v-if="expense.isEditing || expense.isNew" @click="cancelEdit(index)"
                                    class="btn btn-secondary btn-sm" type="button">
                                    <i class="fas fa-times"></i> Cancel
                                </button>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>

            <!-- Empty State -->
            <div v-if="store.expenses.length === 0 && displayExpense.length === 0" class="text-center py-5">
                <div class="mb-3">
                    <i class="fas fa-users fa-3x text-muted"></i>
                </div>
                <h5 class="text-muted">No Expense found</h5>
                <p class="text-muted">Start by adding your first expense</p>
                <button @click="addNewExpense" class="btn btn-primary">
                    <i class="fas fa-plus me-2"></i>Add Expense
                </button>
            </div>


        </div>
    </div>

</template>
<script setup>
import { ref, onMounted, computed } from 'vue';
import { useExpenseStore } from '@/stores/finance/expenseStore';

const store = useExpenseStore();
const errors = ref({});
const Loading = ref(true);
const isSaving = ref(false)
const originalData = ref({})

const displayExpense = computed(() => {
    return store.expenses.map(expense => ({
        ...expense,
        isEditing: expense.isEditing || false,
        isNew: expense.isNew || false
    }));
});

onMounted(async () => {

    await store.fetchExpenses();

});

const addNewExpense = () => {
    const newExpense = {
        id: Date.now(),
        expense_date: new Date().toISOString().split('T')[0],
        amount: 0,
        description: '',
        expense_number: '',
        vendor: '',
        tax_amount: 0,
        expense_account: '',
        payment_method: '',
        journal_entry: '',
        notes: '',
        created_at: new Date().toISOString(),
        updated_at: new Date().toISOString(),
        isNew: true,
        isEditing: true,
    };
    store.expenses.push(newExpense);

};

const editExpense = (index) => {
    store.expenses[index].isEditing = true;
    originalData.value[index] = { ...store.expenses[index] };
};

const cancelEdit = (index) => {
    const expense = store.expenses[index];
    if (expense.isNew) {
        store.expenses.splice(index, 1); // Remove new expense if cancelled
    } else {
        // Revert to original data
        if (originalData.value[index]) {
            Object.assign(store.expenses[index], originalData.value[index])
            delete originalData.value[index]

        }
        store.expenses[index].isEditing = false
    }
    clearRowErrors(index)
};

const handleSave = async (expense, index) => {
    try {
        isSaving = true
        clearRowErrors(index)
        if (!validateExpense(expense, index)) {
            isSaving.value = false
            return
        }
        const expenseData = {
            id: Date.now(),
            expense_date: expense.expense_date.date() || Date.now(),
            amount: expense.amount || 0,
            description: expense.description?.trim() || '',
            expense_number: expense.expense_number || '',
            vendor: expense.vendor?.time() || '',
            tax_amount: expense.tax_amount || 0,
            expense_account: expense.expense_account?.trim() || '',
            payment_method: expense.payment_method || '',
            journal_entry: expense.journal_entry || '',
            notes: expense.notes?.trim() || '',
            created_at: expense.created_at || '',
            updated_at: expense.updated_at || ''

        }
        if (expense.isNew) {
            await store.addExpense(expenseData)
            store.expenses.splice(index, 1)
            await store.fetchExpenses()
        } else {

            await store.updateExpense(expense.id, expenseData)
            delete originalData.value[index]
        }
        console.log(`Expense ${expense.isNew ? 'created' : 'updated'} successfully!`)
    } catch (error) {
        console.error('Error saving expense:', error)

        // Handle validation errors from backend
        if (error.response?.status === 400 && error.response.data) {
            handleBackendErrors(error.response.data, index)
        } else {
            // Show error message
            alert('Failed to save expense. Please try again.')
        }
    } finally {
        isSaving.value = false
    }
}

const validateExpense = (expense, index) => {
    let isValid = true

    // Required field validation
    if (!expense.expense_date) {
        errors.value[`${index}.expense_date`] = 'Expense date is required'
        isValid = false
    }

    if (!expense.amount || expense.amount <= 0) {
        errors.value[`${index}.amount`] = 'Amount is required and must be greater than 0'
        isValid = false
    }

    if (!expense.description?.trim()) {
        errors.value[`${index}.description`] = 'Description is required'
        isValid = false
    }

    if (!expense.vendor?.trim()) {
        errors.value[`${index}.vendor`] = 'Vendor is required'
        isValid = false
    }

    // Optional validation for tax amount (if provided, must be valid)
    if (expense.tax_amount && expense.tax_amount < 0) {
        errors.value[`${index}.tax_amount`] = 'Tax amount cannot be negative'
        isValid = false
    }

    return isValid
}

const validateField = (field, index) => {
    const expense = store.expenses[index] // Adjust this to match your store structure
    const errorKey = `${index}.${field}`

    // Clear existing error
    delete errors.value[errorKey]

    // Validate specific field
    switch (field) {
        case 'expense_date':
            if (!expense.expense_date) {
                errors.value[errorKey] = 'Expense date is required'
            }
            break
        case 'amount':
            if (!expense.amount || expense.amount <= 0) {
                errors.value[errorKey] = 'Amount is required and must be greater than 0'
            }
            break
        case 'description':
            if (!expense.description?.trim()) {
                errors.value[errorKey] = 'Description is required'
            }
            break
        case 'expense_number':
            if (!expense.expense_number?.trim()) {
                errors.value[errorKey] = 'Expense number is required'
            }
            break
        case 'vendor':
            if (!expense.vendor?.trim()) {
                errors.value[errorKey] = 'Vendor is required'
            }
            break
        case 'tax_amount':
            if (expense.tax_amount && expense.tax_amount < 0) {
                errors.value[errorKey] = 'Tax amount cannot be negative'
            }
            break
        case 'expense_account':
            if (!expense.expense_account?.trim()) {
                errors.value[errorKey] = 'Expense account is required'
            }
            break
        case 'payment_method':
            if (!expense.payment_method?.trim()) {
                errors.value[errorKey] = 'Payment method is required'
            }
            break
        case 'journal_entry':
            // Optional field - only validate if you want it required
            if (!expense.journal_entry?.trim()) {
                errors.value[errorKey] = 'Journal entry is required'
            }
            break
        case 'notes':
            // Notes are typically optional, add validation if needed
            break
    }
}

const handleBackendErrors = (backendErrors, index) => {
    Object.keys(backendErrors).forEach(field => {
        const errorKey = `${index}.${field}`
        errors.value[errorKey] = Array.isArray(backendErrors[field])
            ? backendErrors[field][0]
            : backendErrors[field]
    })
}

const clearRowErrors = (index) => {
    Object.keys(errors.value).forEach(key => {
        if (key.startsWith(`${index}.`)) {
            delete errors.value[key]
        }
    })
}

const deleteExpense = async (id, index) => {
    if (confirm('Are you sure you want to delete this expense?his action cannot be undone.')) {
        try {
            await store.removeExpense(id)
        } catch (error) {
            console.error('Error deleting Expense:', error)
            alert('Failed to delete Expense. Please try again.')
        }
    }
}
const formatDate = (dateString) => {
    if (!dateString) return '-'
    return new Date(dateString).toLocaleDateString()
}
</script>

<style scoped>
.table-responsive {
    border-radius: 0.375rem;
    overflow: hidden;
    box-shadow: 0 0.125rem 0.25rem rgba(0, 0, 0, 0.075);
}

.table {
    margin-bottom: 0;
}

.btn-group .btn {
    margin: 0 1px;
}

.text-truncate {
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.table-warning {
    background-color: #fff3cd !important;
}

.form-control-sm,
.form-select-sm {
    min-width: 120px;
}

textarea.form-control-sm {
    min-width: 150px;
    resize: vertical;
}

.invalid-feedback {
    display: block;
    font-size: 0.75rem;
}

@media (max-width: 768px) {
    .table-responsive {
        font-size: 0.875rem;
    }

    .btn-sm {
        padding: 0.25rem 0.5rem;
        font-size: 0.75rem;
    }

    .form-control-sm,
    .form-select-sm {
        min-width: 100px;
    }
}
</style>