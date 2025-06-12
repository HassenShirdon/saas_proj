<template>
    <el-dialog :visible.sync="visible" title="Purchase Order" width="600px" @close="handleClose">
        <el-form :model="form" :rules="rules" ref="formRef" label-width="120px">
            <el-form-item label="PO Number" prop="po_number">
                <el-input v-model="form.po_number" autocomplete="off" />
            </el-form-item>
            <el-form-item label="Supplier" prop="supplier">
                <el-input v-model="form.supplier" autocomplete="off" />
            </el-form-item>
            <el-form-item label="Order Date" prop="order_date">
                <el-date-picker v-model="form.order_date" type="date" placeholder="Select date" style="width: 100%;" />
            </el-form-item>
            <el-form-item label="Delivery Date" prop="delivery_date">
                <el-date-picker v-model="form.delivery_date" type="date" placeholder="Select date"
                    style="width: 100%;" />
            </el-form-item>
            <el-form-item label="Total Amount" prop="total_amount">
                <el-input-number v-model="form.total_amount" :min="0" style="width: 100%;" />
            </el-form-item>
            <el-form-item label="Status" prop="status">
                <el-select v-model="form.status" placeholder="Select status" style="width: 100%;">
                    <el-option label="Pending" value="Pending" />
                    <el-option label="Approved" value="Approved" />
                    <el-option label="Delivered" value="Delivered" />
                    <el-option label="Cancelled" value="Cancelled" />
                </el-select>
            </el-form-item>
            <el-form-item label="Created At" prop="created_at">
                <el-date-picker v-model="form.created_at" type="datetime" placeholder="Select date and time"
                    style="width: 100%;" />
            </el-form-item>
            <el-form-item label="Updated At" prop="updated_at">
                <el-date-picker v-model="form.updated_at" type="datetime" placeholder="Select date and time"
                    style="width: 100%;" />
            </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
            <el-button @click="handleClose">Cancel</el-button>
            <el-button type="primary" @click="handleSubmit">Save</el-button>
        </div>
    </el-dialog>
</template>

<script>
import { ref, reactive, watch, toRefs } from 'vue';
import { usePurchaseOrderStore } from '@/stores/inventory/purchaseOrderStore.js'

export default {
    name: 'PurchaseOrderModal',
    props: {
        visible: {
            type: Boolean,
            required: true
        },
        editData: {
            type: Object,
            default: null
        }
    },
    emits: ['update:visible', 'saved'],
    setup(props, { emit }) {
        const store = usePurchaseOrderStore();
        const formRef = ref(null);

        const form = reactive({
            po_number: '',
            supplier: '',
            order_date: '',
            delivery_date: '',
            total_amount: 0,
            status: '',
            created_at: '',
            updated_at: ''
        });

        const rules = {
            po_number: [{ required: true, message: 'PO Number is required', trigger: 'blur' }],
            supplier: [{ required: true, message: 'Supplier is required', trigger: 'blur' }],
            order_date: [{ required: true, message: 'Order date is required', trigger: 'change' }],
            delivery_date: [{ required: true, message: 'Delivery date is required', trigger: 'change' }],
            total_amount: [{ required: true, message: 'Total amount is required', trigger: 'blur' }],
            status: [{ required: true, message: 'Status is required', trigger: 'change' }],
            created_at: [{ required: true, message: 'Created at is required', trigger: 'change' }],
            updated_at: [{ required: true, message: 'Updated at is required', trigger: 'change' }]
        };

        watch(
            () => props.editData,
            (val) => {
                if (val) {
                    Object.assign(form, val);
                } else {
                    resetForm();
                }
            },
            { immediate: true }
        );

        function resetForm() {
            form.po_number = '';
            form.supplier = '';
            form.order_date = '';
            form.delivery_date = '';
            form.total_amount = 0;
            form.status = '';
            form.created_at = '';
            form.updated_at = '';
        }

        function handleClose() {
            emit('update:visible', false);
            resetForm();
        }

        function handleSubmit() {
            formRef.value.validate(async (valid) => {
                if (valid) {
                    if (props.editData && props.editData.id) {
                        await store.updatePurchaseOrder({ ...form, id: props.editData.id });
                    } else {
                        await store.createPurchaseOrder({ ...form });
                    }
                    emit('saved');
                    handleClose();
                }
            });
        }

        return {
            ...toRefs(form),
            form,
            rules,
            formRef,
            handleClose,
            handleSubmit
        };
    }
};
</script>
<style scoped>
.el-dialog {
    border-radius: 10px;
}

.el-form {
    padding: 10px 0;
}

.el-form-item {
    margin-bottom: 18px;
}

.el-input,
.el-input-number,
.el-select,
.el-date-picker {
    width: 100%;
}

.dialog-footer {
    text-align: right;
    padding: 10px 0 0 0;
}

.el-button+.el-button {
    margin-left: 10px;
}
</style>