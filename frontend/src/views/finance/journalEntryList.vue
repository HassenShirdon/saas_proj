<template>
    <div class="container-fluid p-3 ">
        <div class="container d-flex justify-content-between align-items-center p-4 mb-4 shadow-sm ">
            <h1 class="h2 mb-0 ">Journal Entries</h1>
            <button @click="addNewJournalEntry" class="btn btn-primary" type="button">
                <i class="fas fa-plus me-2"></i>Add Journal Entry
            </button>
        </div>
        <!-- loading state -->
        <div v-if="store.loading" class="text-center py-5">
            <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
            <p class="mt-2 text-muted">Loading Journal Entries...</p>
        </div>

        <div class="table-responsive">
            <table class="table table-striped table-bordered">
                <thead class="table-dark">
                    <tr>
                        <th>#</th>
                        <th>Entry Number</th>
                        <th>Date</th>
                        <th>Description</th>
                        <th>Reference</th>
                        <th>Adjusting</th>
                        <th>Reversing</th>
                        <th>Created At</th>
                        <th>Updated At</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(journalEntry, index) in displayJournalEntries" :key="journalEntry.id || `new-${index}`"
                        :class="{ 'table-warning': journalEntry.isEditing || journalEntry.isNew }">
                        <th scope="row">{{ journalEntry.isNew ? 'NEW' : index + 1 }}</th>

                        <!-- Entry Number -->
                        <td>
                            <input v-if="journalEntry.isEditing || journalEntry.isNew"
                                v-model="journalEntry.entry_number" class="form-control form-control-sm" type="text"
                                :class="{ 'is-invalid': errors[`${index}.entry_number`] }" placeholder="Entry Number"
                                @blur="validateField('entry_number', index)" />
                            <div v-if="errors[`${index}.entry_number`]" class="invalid-feedback">
                                {{ errors[`${index}.entry_number`] }}
                            </div>
                            <span v-else class="fw-semibold">{{ journalEntry.entry_number }}</span>
                        </td>

                        <!-- Date -->
                        <td>
                            <input v-if="journalEntry.isEditing || journalEntry.isNew" v-model="journalEntry.date"
                                type="date" class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.date`] }" placeholder="Date"
                                @blur="validateField('date', index)" />
                            <div v-if="errors[`${index}.date`]" class="invalid-feedback">
                                {{ errors[`${index}.date`] }}
                            </div>
                            <span v-else class="fw-semibold">{{ journalEntry.date }}</span>
                        </td>

                        <!-- Description -->
                        <td>
                            <input v-if="journalEntry.isEditing || journalEntry.isNew"
                                v-model="journalEntry.description" type="text" class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.description`] }" placeholder="Description"
                                @blur="validateField('description', index)" />
                            <div v-if="errors[`${index}.description`]" class="invalid-feedback">
                                {{ errors[`${index}.description`] }}
                            </div>
                            <span v-else class="fw-semibold">{{ journalEntry.description }}</span>
                        </td>

                        <!-- Reference -->
                        <td>
                            <input v-if="journalEntry.isEditing || journalEntry.isNew" v-model="journalEntry.reference"
                                type="text" class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.reference`] }" placeholder="Reference"
                                @blur="validateField('reference', index)" />
                            <div v-if="errors[`${index}.reference`]" class="invalid-feedback">
                                {{ errors[`${index}.reference`] }}
                            </div>
                            <span v-else class="fw-semibold">{{ journalEntry.reference }}</span>
                        </td>

                        <!-- Adjusting -->
                        <td>
                            <select v-if="journalEntry.isEditing || journalEntry.isNew"
                                v-model="journalEntry.is_adjusting" class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.is_adjusting`] }"
                                @blur="validateField('is_adjusting', index)">
                                <option :value="true">True</option>
                                <option :value="false">False</option>
                            </select>
                            <div v-if="errors[`${index}.is_adjusting`]" class="invalid-feedback">
                                {{ errors[`${index}.is_adjusting`] }}
                            </div>
                            <span v-else>{{ journalEntry.is_adjusting ? 'Yes' : 'No' }}</span>
                        </td>

                        <!-- Reversing -->
                        <td>
                            <select v-if="journalEntry.isEditing || journalEntry.isNew"
                                v-model="journalEntry.is_reversing" class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.is_reversing`] }"
                                @blur="validateField('is_reversing', index)">
                                <option :value="true">True</option>
                                <option :value="false">False</option>
                            </select>
                            <div v-if="errors[`${index}.is_reversing`]" class="invalid-feedback">
                                {{ errors[`${index}.is_reversing`] }}
                            </div>
                            <span v-else>{{ journalEntry.is_reversing ? 'Yes' : 'No' }}</span>
                        </td>

                        <!-- Created At -->
                        <td>
                            <input v-if="journalEntry.isEditing || journalEntry.isNew" v-model="journalEntry.created_at"
                                type="date" class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.created_at`] }" placeholder="Created At"
                                @blur="validateField('created_at', index)" />
                            <div v-if="errors[`${index}.created_at`]" class="invalid-feedback">
                                {{ errors[`${index}.created_at`] }}
                            </div>
                            <span v-else class="fw-semibold">{{ journalEntry.created_at }}</span>
                        </td>

                        <!-- Updated At -->
                        <td>
                            <input v-if="journalEntry.isEditing || journalEntry.isNew" v-model="journalEntry.updated_at"
                                type="date" class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.updated_at`] }" placeholder="Updated At"
                                @blur="validateField('updated_at', index)" />
                            <div v-if="errors[`${index}.updated_at`]" class="invalid-feedback">
                                {{ errors[`${index}.updated_at`] }}
                            </div>
                            <span v-else class="fw-semibold">{{ journalEntry.updated_at }}</span>
                        </td>

                        <!-- Actions -->
                        <td>
                            <div class="btn-group" role="group">
                                <button v-if="journalEntry.isEditing || journalEntry.isNew" @click="handleSave(index)"
                                    class="btn btn-success btn-sm">
                                    <i class="fas fa-save"></i> Save
                                </button>
                                <button v-else @click="editJournalEntry(index)" class="btn btn-warning btn-sm">
                                    <i class="fas fa-edit"></i> Edit
                                </button>
                                <button v-if="!journalEntry.isNew" @click="deleteJournalEntry(index)"
                                    class="btn btn-danger btn-sm">
                                    <i class="fas fa-trash"></i> Delete
                                </button>
                                <button v-if="journalEntry.isEditing || journalEntry.isNew" @click="cancelEdit(index)"
                                    class="btn btn-secondary btn-sm">
                                    <i class="fas fa-times"></i> Cancel
                                </button>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>

            <div v-if="store.journalEntries.length === 0 && displayJournalEntries.length === 0"
                class="text-center py-5">
                <div class="mb-3">
                    <i class="fas fa-users fa-3x text-muted"></i>
                </div>
                <h5 class="text-muted">No Journal Entries found</h5>
                <p class="text-muted">Start by adding your first Journal Entry</p>
                <button @click="addNewJournalEntry" class="btn btn-primary">
                    <i class="fas fa-plus me-2"></i>Add Journal Entry
                </button>
            </div>

        </div>

    </div>

</template>
<script setup>
import { onMounted, ref, computed } from 'vue';
import { useJournalEntryStore } from '@/stores/finance/journalEntryStore';
const store = useJournalEntryStore();
const journalEntries = ref([]);
const loading = ref(true);
const errors = ref({});
const originalData = ref({});


const displayJournalEntries = computed(() => {
    return store.journalEntries.map(journalEntry => ({
        ...journalEntry,
        isEditing: journalEntry.isEditing || false,
        isNew: journalEntry.isNew || false,
    }));
});

onMounted(async () => {
    await store.fetchJournalEntries();
})

const addNewJournalEntry = () => {
    const newJournalEntry = {
        id: null,
        entry_number: '',
        date: new Date().toISOString().split('T')[0],
        description: '',
        reference: '',
        is_adjusting: false,
        is_reversing: true,
        created_at: new Date().toISOString(),
        updated_at: new Date().toISOString(),
    };
    store.journalEntries.unshift(newJournalEntry);
}
const editJournalEntry = (journalEntry) => {
    originalData.value[index] = {
        ...store.journalEntries[index]
    };
    store.journalEntries[index].isEditing = true
}

const cancelEdit = (index) => {
    const journalEntry = store.journalEntries[index];
    if (journalEntry.isNew) {
        store.journalEntries.splice(index, 1);
    } else {
        if (originalData.value[index]) {
            // Restore the original data
            Object.assign(journalEntry, originalData.value[index]);
            delete originalData.value[index];
        }
        store.journalEntries[index].isEditing = false;
    }
    clearRowErrors(index);
}

const handleSave = async (journalEntry, index) => {
    try {
        isSaving.value = true;
        clearRowErrors(index);
        if (!validateJournalEntry(journalEntry, index)) {
            isSaving.value = false;
            return;
        }

        const journalEntryData = {
            date: journalEntry.date || '',
            entry_number: journalEntry.entry_number || '',
            description: journalEntry.description || '',
            reference: journalEntry.reference || '',
            is_adjusting: journalEntry.is_adjusting || false,
            is_reversing: journalEntry.is_reversing || false,
            created_at: journalEntry.created_at || new Date().toISOString(),
            updated_at: new Date().toISOString(),
        }
        if (journalEntry.isNew) {
            await store.AddJournalEntry(journalEntryData);
            store.journalEntries.splice(index, 1)
            await store.fetchJournalEntries();
        } else {
            await store.updateJournalEntry(journalEntry.id, journalEntryData);
            delete originalData.value[index]
        }
        console.log(`JournalEntry ${journalEntry.isNew ? 'created' : 'updated'} successfully!`)
    } catch (error) {
        console.log(`Error saving journal entry: ${error}`);

        if (error.response?.status === 400 && error.response.data) {
            handleBackendErrors(error.response.data, index)
        } else {
            // Show error message
            alert('Failed to save Journal Entry. Please try again.')
        }
    } finally {
        isSaving.value = false;
    }

}
const validateJournalEntry = (entry, index) => {
    let isValid = true;

    if (!entry.entry_number?.trim()) {
        errors.value[`${index}.entry_number`] = 'Entry number is required';
        isValid = false;
    }

    if (!entry.date) {
        errors.value[`${index}.date`] = 'Entry date is required';
        isValid = false;
    }

    if (!entry.description?.trim()) {
        errors.value[`${index}.description`] = 'Description is required';
        isValid = false;
    }

    // Optional: Validate reference if you want it required
    // if (!entry.reference?.trim()) {
    //     errors.value[`${index}.reference`] = 'Reference is required';
    //     isValid = false;
    // }

    return isValid;
};
const validateJournalField = (field, index) => {
    const entry = store.journalEntries[index]; // Adjust based on your store
    const errorKey = `${index}.${field}`;

    // Clear any existing error
    delete errors.value[errorKey];

    switch (field) {
        case 'entry_number':
            if (!entry.entry_number?.trim()) {
                errors.value[errorKey] = 'Entry number is required';
            }
            break;
        case 'date':
            if (!entry.date) {
                errors.value[errorKey] = 'Entry date is required';
            }
            break;
        case 'description':
            if (!entry.description?.trim()) {
                errors.value[errorKey] = 'Description is required';
            }
            break;
        case 'reference':
            // Optional: enable if reference is required
            // if (!entry.reference?.trim()) {
            //     errors.value[errorKey] = 'Reference is required';
            // }
            break;
    }
};

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

const deleteJournalEntry = async (id, index) => {
    if (confirm('Are you sure you want to dlete this Journal Entry?his action cannot be undone.')) {
        try {
            await store.removeJournalEntry(id)
        } catch (error) {
            console.error('Error deleting Journal Entry:', error)
            alert('Failed to delete Journal Entry. Please try again.')
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
