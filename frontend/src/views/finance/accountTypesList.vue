<template>
    <div class="container-fluid p-2">

        <div class="d-flex justify-content-between p-4 align-items-center mb-4">
            <h1 class="h2 mb-0">Account Types </h1>
            <button @click="addNewAccountType" class="btn btn-primary" type="button">
                <i class="fas fa-plus me-2"></i>Add Account Type
            </button>
        </div>
        <!-- loading State -->
        <div v-if="store.loading" class="text-center py-5">
            <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
            <p class="mt-2 text-muted">Loading Account Types...</p>
        </div>

        <div v-else class="table-responsive">
            <table class="table table-striped table-bordered p-2">
                <thead class="table-dark">
                    <tr>
                        <th>S. No</th>
                        <th>Account Name</th>
                        <th>Normal Balance</th>
                        <th>Category</th>
                        <th>Description</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                </tbody>
            </table>
        </div>

    </div>

</template>
<script setup>
import { ref, onMounted, computed } from 'vue';
import { useAccountTypeStore } from '@/stores/finance/accountTypeStore';

const store = useAccountTypeStore();
const errors = ref({});
const loading = ref(true)
const originalData = ref({});

const displayAccountTypes = computed(() => {
    return store.accountTypes.map(accountType => ({
        ...accountType,
        isEditing: accountType.isEditing || false,
        isNew: accountType.isNew || false
    }))
})

onMounted(async () => {
    await store.fetchAccountTypes();
});

const addAccountType = () => {
    const newAccountType = {
        id: '',
        name: '',
        normal_balance: '',
        category: '',
        description: ''
    };
    store.accountTypes.push(newAccountType);
};

const editAccountType = (index) => {
    store.accountTypes[index].isEditing = true;
    originalData.value[index] = { ...store.accountTypes[index] };
};

const cancelEdit = (index) => {
    const accountType = store.accountTypes[index];
    if (accountType.isNew) {
        store.accountTypes.splice(index, 1)
    } else {
        if (originalData.value[index]) {
            Object.assign(store.accountTypes[index], originalData.value[index])
            delete originalData.value[index]
        }
        store.accountTypes[index].isEditing = false
    }
    clearRowErrors(index)
}

const handleSave = async (accountType, index) => {
    try {
        isSaving = true
        clearRowErrors(index)
        if (!validteAccountType(accountType, index)) {
            isSaving.value = false
            return
        }
        const accountTypeData = {
            id: Date.now(),
            name: accountType.name || '',
            normal_balance: accountType.normal_balance || '',
            category: accountType.category || '',
            description: accountType.description || ''

        }
        if (accountTypeData.isNew) {
            await store.addAccountType(accountTypeData)
            store.accountTypes.splice(index, 1)
            await store.fetchAccountTypes
        } else {
            await store.updateAccountTypes(accountType.id, accountTypeData)
            delete originalData.value[index]
        }
        console.log(`accountType ${accountType.isNew ? 'created' : 'updated'} successfully`)

    } catch (error) {
        console.error('Error saving accountType:', error)

        // Handle validation errors from backend
        if (error.response?.status === 400 && error.response.data) {
            handleBackendErrors(error.response.data, index)
        } else {
            // Show error message
            alert('Failed to save accountType. Please try again.')
        }
    } finally {
        isSaving.value = false
    }
}

const validateAccountType = (accountType, index) => {
    let isValid = true

    if (!accountType.name?.trim()) {
        errors.value[`${index}.name`] = 'Account name is required'
        isValid = false
    }

    if (!accountType.normal_balance?.trim()) {
        errors.value[`${index}.normal_balance`] = 'Normal balance is required'
        isValid = false
    }

    if (!accountType.category?.trim()) {
        errors.value[`${index}.category`] = 'Category is required'
        isValid = false
    }

    if (!accountType.description?.trim()) {
        errors.value[`${index}.description`] = 'Description is required'
        isValid = false
    }

    return isValid
}

const validateAccountField = (field, index) => {
    const accountType = store.accountTypes[index] // Adjust if your structure differs
    const errorKey = `${index}.${field}`

    // Clear existing error
    delete errors.value[errorKey]

    switch (field) {
        case 'name':
            if (!accountType.name?.trim()) {
                errors.value[errorKey] = 'Account name is required'
            }
            break
        case 'normal_balance':
            if (!accountType.normal_balance?.trim()) {
                errors.value[errorKey] = 'Normal balance is required'
            }
            break
        case 'category':
            if (!accountType.category?.trim()) {
                errors.value[errorKey] = 'Category is required'
            }
            break
        case 'description':
            if (!accountType.description?.trim()) {
                errors.value[errorKey] = 'Description is required'
            }
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
const deleteAccountType = async (id, index) => {
    if (confirm('Are you sure you want to dlete this Acount type?his action cannot be undone.')) {
        try {
            await store.removeAccountType(id)
        } catch (error) {
            console.error('Error deleting Acount type:', error)
            alert('Failed to delete Acount type. Please try again.')
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