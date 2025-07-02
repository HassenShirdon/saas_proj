<template>
    <div class="container-fluid p-2">
        <div class="container d-flex justify-content-between align-items-center p-4 mb-4 shadow-sm">
            <h1 class="h2 mb-0">Journal Lines</h1>
            <button @click="addNewJournalEntryLine" class="btn btn-primary" type="button">
                <i class="fas fa-plus me-2"></i>Add Journal Entry Line
            </button>
        </div>

        <!-- Loading State -->
        <div v-if="store.loading" class="text-center py-5">
            <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
            <p class="mt-2 text-muted">Loading journal Entry lines...</p>
        </div>

        <!-- Journal Lines Table -->
        <div v-else class="table-responsive">
            <table class="table table-striped table-hover">
                <thead class="table-dark">
                    <tr>
                        <th>#</th>
                        <th>Journal Entry</th>
                        <th>Account</th>
                        <th>Amount</th>
                        <th>Type</th>
                        <th>Description</th>
                        <th>Reference</th>
                        <th class="text-center">Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(line, index) in store.displayJournalEntryLines" :key="line.id || `new-${index}`"
                        :class="{ 'table-warning': line.isEditing || line.isNew }">
                        <th scope="row">{{ line.isNew ? 'NEW' : index + 1 }}</th>

                        <!-- Journal Entry -->
                        <td>
                            <input v-if="line.isEditing || line.isNew" v-model="line.journal_entry" type="text"
                                class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.journal_entry`] }"
                                placeholder="Journal Entry ID" @blur="validateField(index, 'journal_entry')" />
                            <div v-if="errors[`${index}.journal_entry`]" class="invalid-feedback">
                                {{ errors[`${index}.journal_entry`] }}
                            </div>
                            <span v-else>{{ line.journal_entry }}</span>
                        </td>

                        <!-- Account -->
                        <td>
                            <input v-if="line.isEditing || line.isNew" v-model="line.account" type="number"
                                class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.account`] }" placeholder="Account ID"
                                @blur="validateField(index, 'account')" />
                            <div v-if="errors[`${index}.account`]" class="invalid-feedback">
                                {{ errors[`${index}.account`] }}
                            </div>
                            <span v-else>{{ line.account }}</span>
                        </td>

                        <!-- Amount -->
                        <td>
                            <input v-if="line.isEditing || line.isNew" v-model.number="line.amount" type="number"
                                step="0.01" class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.amount`] }" placeholder="0.00"
                                @blur="validateField(index, 'amount')" />
                            <div v-if="errors[`${index}.amount`]" class="invalid-feedback">
                                {{ errors[`${index}.amount`] }}
                            </div>
                            <span v-else>{{ line.amount }}</span>
                        </td>

                        <!-- Debit or Credit -->
                        <td>
                            <!-- Editable state -->
                            <select v-if="line.isEditing || line.isNew" v-model="line.is_debit"
                                class="form-select form-select-sm">
                                <option :value="true">Debit</option>
                                <option :value="false">Credit</option>
                            </select>

                            <!-- Read-only state -->
                            <span v-else :class="line.is_debit ? 'text-success' : 'text-danger'">
                                {{ line.is_debit ? 'Debit' : 'Credit' }}
                            </span>
                        </td>

                        <!-- Description -->
                        <td>
                            <textarea v-if="line.isEditing || line.isNew" v-model="line.description"
                                class="form-control form-control-sm" rows="2" placeholder="Description"></textarea>
                            <span v-else class="text-muted" :title="line.description || '-'">
                                {{ line.description || '-' }}
                            </span>
                        </td>

                        <!-- Reference -->
                        <td>
                            <input v-if="line.isEditing || line.isNew" v-model="line.reference" type="text"
                                class="form-control form-control-sm" placeholder="Reference" />
                            <span v-else class="text-muted">{{ line.reference || '-' }}</span>
                        </td>

                        <!-- Actions -->
                        <td class="text-center">
                            <div v-if="line.isEditing || line.isNew" class="btn-group" role="group">
                                <button @click="handleSave(line, index)" class="btn btn-success btn-sm"
                                    :disabled="isSaving" title="Save Line">
                                    <i class="bi bi-check-lg"></i>
                                </button>
                                <button @click="cancelEdit(index)" class="btn btn-secondary btn-sm" title="Cancel">
                                    <i class="bi bi-x-lg"></i>
                                </button>
                            </div>
                            <div v-else class="btn-group" role="group">
                                <button @click="editJournalLine(index)" class="btn btn-outline-primary btn-sm me-2"
                                    title="Edit Line">
                                    <i class="bi bi-pencil"></i>
                                </button>
                                <button @click="deleteJournalLine(line.id, index)" class="btn btn-outline-danger btn-sm"
                                    title="Delete">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>

            <!-- Empty State -->
            <div v-if="store.journalEntryLines.length === 0" class="text-center py-5">
                <div class="mb-3">
                    <i class="fas fa-book fa-3x text-muted"></i>
                </div>
                <h5 class="text-muted">No journal lines found</h5>
                <p class="text-muted">Start by adding a new journal line</p>
                <button @click="addNewJournalEntryLine" class="btn btn-primary">
                    <i class="fas fa-plus me-2"></i>Add Line
                </button>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { useJournalEntryLineStore } from '@/stores/finance/journalEntryLineStore';

const store = useJournalEntryLineStore();
const journalEntryLines = ref([]);
const errors = ref({});
const isSaving = ref(false);
const origingalData = ref({});

const displayJournalEntryLines = computed(() => {
    return journalEntryLines.value.map(line => ({
        ...line,
        isEditing: journalEntryLine.isEditing || false,
        isNew: journalEntryLine.isNew || false
    }));
});

onMounted(async () => {
    await store.fetchJournalEntryLines();
});

const addNewJournalEntryLine = () => {
    const newJournalEntryLine = {
        journal_entry: null,
        account: null,
        amount: 0.00,
        is_debit: true,
        description: '',
        reference: '',
        isNew: true,
        isEditing: true
    };
    store.journalEntryLines.unshift(newJournalEntryLine);

}

const cancelEdit = (index) => {
    const journalEntryLine = store.journalEntryLines[index];
    if (journalEntryLine.isNew) {
        store.journalEntryLines.splice(index, 1);
    } else {
        if (origingalData.value[index]) {
            Object.assign(store.journalEntryLines[index],
                originalData.value[index])
            delete originalData.value[index]

        }
        store.journalEntryLines[index].isEditing = false
    }
    clearRowsErrors(index);
}

const handleSave = async (journalEntryLine, index) => {
    try {
        isSaving.value = true;
        clearRowsErrors(index);
        if (!validateJournalEntryLine(journalEntryLine, index)) {
            return;
        }
        const journalEntryLineData = {
            journal_entry: journalLine.journal_entry,
            account: journalLine.account,
            amount: parseFloat(journalLine.amount) || 0.00,
            is_debit: journalLine.is_debit,
            description: journalLine.description?.trim() || '',
            reference: journalLine.reference?.trim() || ''
        };
        if (journalEntryLine.isNew) {
            await store.createJournalEntryLine(journalEntryLineData);
            store.journalEntryLines.splice(index, 1);
            await store.fetchJournalEntryLines();
        } else {
            await store.updateJournalEntryLine(journalEntryLine.id, journalEntryLineData);
            store.journalEntryLines[index].isEditing = false;
            delete origingalData.value[index];
        }
        console.log(`journalEntryLine ${journalEntryLine.isNew ? 'created' : 'updated'} successfully!`)

    } catch (error) {
        console.error('Error saving journalEntryLine:', error)

        // Handle validation errors from backend
        if (error.response?.status === 400 && error.response.data) {
            handleBackendErrors(error.response.data, index)
        } else {
            // Show error message
            alert('Failed to save journalEntryLine. Please try again.')
        }
    } finally {
        isSaving.value = false
    }
}

const validateJournalLine = (journalLine, index) => {
    let isValid = true;

    if (!journalLine.journal_entry) {
        errors.value[`${index}.journal_entry`] = 'Journal entry is required';
        isValid = false;
    }

    if (!journalLine.account) {
        errors.value[`${index}.account`] = 'Account is required';
        isValid = false;
    }

    if (journalLine.amount === null || journalLine.amount === undefined || isNaN(journalLine.amount)) {
        errors.value[`${index}.amount`] = 'Amount is required';
        isValid = false;
    }

    return isValid;
};

const validateField = (index, field) => {
    const journalLine = store.journalLines[index];
    const errorKey = `${index}.${field}`;

    // Clear existing error
    delete errors.value[errorKey];

    switch (field) {
        case 'journal_entry':
            if (!journalLine.journal_entry) {
                errors.value[errorKey] = 'Journal entry is required';
            }
            break;
        case 'account':
            if (!journalLine.account) {
                errors.value[errorKey] = 'Account is required';
            }
            break;
        case 'amount':
            if (journalLine.amount === null || journalLine.amount === undefined || isNaN(journalLine.amount)) {
                errors.value[errorKey] = 'Amount is required';
            }
            break;
    }
};
const clearRowsErrors = (index) => {
    Object.keys(errors.value).forEach(key => {
        if (key.startsWith(`${index}.`)) {
            delete errors.value[key];
        }
    });
};

const handleBackendErrors = (errorData, index) => {
    if (errorData.errors) {
        Object.keys(errorData.errors).forEach(field => {
            errors.value[`${index}.${field}`] = errorData.errors[field][0];
        });
    } else {
        alert('An unexpected error occurred. Please try again.');
    }
};

const deleteJournalEntryLine = async (id, index) => {

    if (confirm(`Are you sure you want to delete this journal entry line?`)) {
        try {
            await store.deleteJournalEntryLine(journalEntryLine.id);
        } catch (error) {
            console.error('Error deleting journal entry line:', error);
            alert('Failed to delete journal entry line. Please try again.');
        }
    }
};
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