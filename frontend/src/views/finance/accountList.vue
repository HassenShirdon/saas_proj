<template>
    <div class="container-fluid p-2">
        <div class="d-flex justify-content-between align-items-center mb-4">
            <h1 class="h2 mb-0">Accounts</h1>
            <button @click="addNewAccount" class="btn btn-primary" type="button">
                <i class="fas fa-plus me-2"></i>Add Account
            </button>
        </div>
        <!-- loading State -->
        <div v-if="store.loading" class="text-center py-5">
            <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
            <p class="mt-2 text-muted">Loading accounts...</p>
        </div>

        <div v-else class="table-responsive">
            <table class="table table-striped table-hover">
                <thead class="table-dark">
                    <tr>
                        <th>Code</th>
                        <th>Name</th>
                        <th>Description</th>
                        <th>Type</th>
                        <th>Parent Account</th>
                        <th>Opening Balance</th>
                        <th>Current Balance</th>
                        <th>Created At</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="account in displayAccounts" :key="account.id || `new-${index}`"
                        :class="{ 'table-warning': account.isEditing || account.isNew }">
                        <th scope="row">{{ account.isNew ? 'NEW' : index + 1 }}</th>

                        <td>
                            <input v-if="account.isEditing || account.isNew" v-model="account.name" type="text"
                                class="form-control form-control-sm" :class="{ 'is-invalid': errors[`${index}.name`] }"
                                placeholder="account name" @blur="validateField(index, 'name')" />
                            <div v-if="errors[`${index}.name`]" class="invalid-feedback">
                                {{ errors[`${index}.name`] }}
                            </div>
                            <span v-else class="fw-semibold">{{ account.name }}</span>
                        </td>

                        <!-- account description -->
                        <td>
                            <input v-if="account.isEditing || account.isNew" v-model="account.description" type="text"
                                class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.description`] }"
                                placeholder="account description" @blur="validateField(index, 'description')" />
                            <div v-if="errors[`${index}.description`]" class="invalid-feedback">
                                {{ errors[`${index}.description`] }}
                            </div>
                            <span v-else class="fw-semibold">{{ account.description }}</span>
                        </td>

                        <td>
                            <input v-if="account.isEditing || account.isNew" v-model="account.account_type" type="text"
                                class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.account_type`] }" placeholder="Account Type"
                                @blur="validateField(index, 'account_type')" />
                            <div v-if="errors[`${index}.account_type`]" class="invalid-feedback">
                                {{ errors[`${index}.account_type`] }}
                            </div>
                            <span v-else class="fw-semibold">{{ account.account_type }}</span>
                        </td>
                        <td>
                            <input v-if="account.isEditing || account.isNew" v-model="account.parent_account"
                                type="text" class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.parent_account`] }"
                                placeholder="Parent Account" @blur="validateField(index, 'parent_account')" />
                            <div v-if="errors[`${index}.parent_account`]" class="invalid-feedback">
                                {{ errors[`${index}.parent_account`] }}
                            </div>
                            <span v-else class="fw-semibold">{{ account.parent_account }}</span>
                        </td>

                        <td>
                            <input v-if="account.isEditing || account.isNew" v-model.number="account.opening_balance"
                                type="number" step="0.01" class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.opening_balance`] }"
                                placeholder="Opening Balance" @blur="validateField(index, 'opening_balance')" />
                            <div v-if="errors[`${index}.opening_balance`]" class="invalid-feedback">
                                {{ errors[`${index}.opening_balance`] }}
                            </div>
                            <span v-else class="fw-semibold">{{ account.opening_balance }}</span>
                        </td>
                        <td>
                            <input v-if="account.isEditing || account.isNew" v-model.number="account.current_balance"
                                type="number" step="0.01" class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.current_balance`] }"
                                placeholder="Current Balance" @blur="validateField(index, 'current_balance')" />
                            <div v-if="errors[`${index}.current_balance`]" class="invalid-feedback">
                                {{ errors[`${index}.current_balance`] }}
                            </div>
                            <span v-else class="fw-semibold">{{ account.current_balance }}</span>
                        </td>

                        <td>
                            <input v-if="account.isEditing || account.isNew" v-model="account.createdAt" type="date"
                                class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.createdAt`] }" placeholder="Created At"
                                @blur="validateField(index, 'createdAt')" />
                            <div v-if="errors[`${index}.createdAt`]" class="invalid-feedback">
                                {{ errors[`${index}.createdAt`] }}
                            </div>
                            <span v-else class="fw-semibold">{{ account.createdAt }}</span>
                        </td>

                        <td>
                            <input v-if="account.isEditing || account.isNew" v-model="account.is_active" type="checkbox"
                                class="form-check-input" @change="validateField(index, 'is_active')" />
                            <span v-else class="fw-semibold">{{ account.is_active ? 'Active' : 'Inactive' }}</span>
                        </td>

                        <!-- Actions -->
                        <td class="text-center">
                            <div v-if="account.isEditing || account.isNew" class="btn-group" role="group">
                                <button @click="handleSave(account, index)" class="btn btn-success btn-sm"
                                    :disabled="isSaving" title="Save Account">
                                    <i class="bi bi-check-lg"></i>
                                </button>
                                <button @click="cancelEdit(index)" class="btn btn-secondary btn-sm" title="Cancel">
                                    <i class="bi bi-x-lg"></i>
                                </button>
                            </div>
                            <div v-else class="btn-group" role="group">
                                <button @click="editAccount(index)" class="btn btn-outline-primary btn-sm me-2"
                                    title="Edit Account">
                                    <i class="bi bi-pencil"></i>
                                </button>
                                <button @click="deleteAccount(Account.id, index)" class="btn btn-outline-danger btn-sm"
                                    title="Delete">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </div>
                        </td>
                    </tr>
                </tbody>

            </table>

            <!-- Empty State -->

            <div v-if="store.accounts.length === 0 && displayAccounts.length === 0" class="text-center py-5">
                <div class="mb-3">
                    <i class="fas fa-users fa-3x text-muted"></i>
                </div>
                <h5 class="text-muted">No Accounts found</h5>
                <p class="text-muted">Start by adding your first account</p>
                <button @click="addNewAccount" class="btn btn-primary">
                    <i class="fas fa-plus me-2"></i>Add Account
                </button>
            </div>
        </div>
    </div>
</template>
<script setup>
import { ref, onMounted, computed } from 'vue';
import { useAccountStore } from '@/stores/finance/accountStore';

const store = useAccountStore();
const error = ref(null);
const loading = ref(true);
const originalData = ref({});

const displayAccounts = computed(() => {
    return store.accounts.map(account => ({
        ...account,
        balance: account.balance,
        createdAt: new Date(account.createdAt).toLocaleDateString(),
    }));
});

onMounted(async () => {
    try {
        loading.value = true;
        await store.fetchAccounts();
    } catch (err) {
        error.value = 'Failed to load accounts';
    } finally {
        loading.value = false;
    }
});
const addNewAccount = () => {
    const newAccount = {
        code: null,
        name: '',
        descriptio: '',
        is_active: false,
        opening_balance: null,
        current_balance: null,
        account_type: null,
        parent_account: null
    };
    store.accounts.unshift(newAccount)
}
const editAccount = (index) => {
    store.accounts[index].isEditing = true;
    originalData.value[index] = { ...store.accounts[index] };
};
const cancelEdit = (index) => {
    store.accounts[index] = { ...originalData.value[index] };
    store.accounts[index].isEditing = false;
};
const validateField = (index, field) => {
    const account = store.accounts[index];
    if (!account[field]) {
        store.errors[`${index}.${field}`] = `${field.replace('_', ' ')} is required`;
    } else {
        delete store.errors[`${index}.${field}`];
    }
};
const handleSave = async (account, index) => {
    if (store.isSaving) return;
    store.isSaving = true;

    try {
        await store.saveAccount(account);
        store.accounts[index].isEditing = false;
        delete store.errors[`${index}.name`];
        delete store.errors[`${index}.description`];
        delete store.errors[`${index}.account_type`];
        delete store.errors[`${index}.parent_account`];
        delete store.errors[`${index}.opening_balance`];
        delete store.errors[`${index}.current_balance`];
        delete store.errors[`${index}.createdAt`];
    } catch (error) {
        console.error('Error saving account:', error);
    } finally {
        store.isSaving = false;
    }
};
const deleteAccount = async (id, index) => {
    if (store.isSaving) return;
    store.isSaving = true;

    try {
        await store.deleteAccount(id);
        store.accounts.splice(index, 1);
    } catch (error) {
        console.error('Error deleting account:', error);
    } finally {
        store.isSaving = false;
    }
};

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