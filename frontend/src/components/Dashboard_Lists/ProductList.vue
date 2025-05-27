<template>
    <div class="container-fluid py-4">
        <div class="page-header">
            <h1 class="page-title">
                <i class="fas fa-box-open me-2"></i>Product Management
            </h1>
            <button class="btn btn-add text-white">
                <i class="bi bi-house-door-fill"></i>Add Product
            </button>
        </div>

        <div class="card">
            <div class="card-body">
                <div class="row mb-3">
                    <div class="col-md-6">
                        <div class="search-box">
                            <i class="fas fa-search"></i>
                            <input type="text" class="form-control" placeholder="Search products...">
                        </div>
                    </div>
                    <div class="col-md-6 text-end">
                        <div class="btn-group" role="group">
                            <button type="button" class="btn btn-outline-secondary">All</button>
                            <button type="button" class="btn btn-outline-secondary">Active</button>
                            <button type="button" class="btn btn-outline-secondary">Inactive</button>
                        </div>
                        <button class="btn btn-outline-secondary ms-2">
                            <i class="fas fa-filter"></i> Filters
                        </button>
                    </div>
                </div>

                <div class="table-responsive">
                    <table class="table">
                        <thead>
                            <tr>
                                <th>PRODUCT ID</th>
                                <th>NAME</th>
                                <th>CATEGORY</th>
                                <th>DESCRIPTION</th>
                                <th>PRICE</th>
                                <th>SALE PRICE</th>
                                <th>STATUS</th>
                                <th>QUANTITY</th>
                                <th>TOTAL</th>
                                <th class="text-end">ACTIONS</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>

                            </tr>
                        </tbody>
                    </table>
                </div>

                <div class="row mt-3">
                    <div class="col-md-6">
                        <p class="text-muted">Showing 1 to 5 of 5 entries</p>
                    </div>
                    <div class="col-md-6">
                        <nav aria-label="Page navigation" class="float-end">
                            <ul class="pagination">
                                <li class="page-item disabled">
                                    <a class="page-link" href="#" tabindex="-1" aria-disabled="true">Previous</a>
                                </li>
                                <li class="page-item active"><a class="page-link" href="#">1</a></li>
                                <li class="page-item">
                                    <a class="page-link" href="#">Next</a>
                                </li>
                            </ul>
                        </nav>
                    </div>
                </div>
            </div>
        </div>
    </div>


</template>
<script setup>
</script>
<style>
.page-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 30px;
    padding: 20px 0;
    border-bottom: 1px solid #e0e0e0;
}

.page-title {
    font-size: 1.8rem;
    font-weight: 600;
    color: var(--dark-color);
    margin: 0;
}

.btn-add {
    background-color: var(--primary-color);
    border: none;
    padding: 10px 20px;
    border-radius: 6px;
    font-weight: 500;
    transition: all 0.3s;
}

.btn-add:hover {
    background-color: var(--primary-hover);
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(115, 103, 240, 0.3);
}

.card {
    border: none;
    border-radius: 10px;
    box-shadow: 0 4px 24px 0 rgba(34, 41, 47, 0.1);
    overflow: hidden;
}

.table-responsive {
    border-radius: 10px;
    overflow: hidden;
}

.table {
    margin-bottom: 0;
}

.table thead th {
    background-color: #f3f2f7;
    color: var(--dark-color);
    font-weight: 600;
    border-bottom-width: 1px;
    padding: 15px 20px;
    vertical-align: middle;
}

.table tbody td {
    padding: 15px 20px;
    vertical-align: middle;
    border-top: 1px solid #f3f2f7;
}

.table tbody tr:hover {
    background-color: rgba(115, 103, 240, 0.05);
}

.badge-category {
    background-color: rgba(115, 103, 240, 0.12);
    color: var(--primary-color);
    font-weight: 500;
    padding: 5px 10px;
    border-radius: 4px;
    font-size: 0.8rem;
}

.price {
    font-weight: 600;
    color: var(--dark-color);
}

.sale-price {
    text-decoration: line-through;
    color: var(--secondary-color);
    font-size: 0.9rem;
}

.action-btns .btn {
    padding: 6px 10px;
    border-radius: 5px;
    font-size: 0.85rem;
    margin: 0 3px;
    transition: all 0.2s;
}

.btn-edit {
    background-color: rgba(40, 199, 111, 0.12);
    color: var(--success-color);
    border: 1px solid rgba(40, 199, 111, 0.3);
}

.btn-edit:hover {
    background-color: var(--success-color);
    color: white;
}

.btn-delete {
    background-color: rgba(234, 84, 85, 0.12);
    color: var(--danger-color);
    border: 1px solid rgba(234, 84, 85, 0.3);
}

.btn-delete:hover {
    background-color: var(--danger-color);
    color: white;
}

.status-active {
    color: var(--success-color);
    font-weight: 500;
}

.status-inactive {
    color: var(--secondary-color);
    font-weight: 500;
}

.search-box {
    position: relative;
    margin-bottom: 20px;
}

.search-box input {
    padding-left: 40px;
    border-radius: 6px;
    border: 1px solid #e0e0e0;
}

.search-box i {
    position: absolute;
    left: 15px;
    top: 12px;
    color: var(--secondary-color);
}
</style>