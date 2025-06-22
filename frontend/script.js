
document.addEventListener("DOMContentLoaded", () => {
    const categorySelect = document.getElementById("category");
    const transactionsTable = document.getElementById("transactionsTable").getElementsByTagName("tbody")[0];

    async function fetchTransactions(category = "") {
        const res = await fetch(`/api/transactions${category ? '?category=' + category : ''}`);
        return await res.json();
    }

    async function fetchSummary() {
        const res = await fetch("/api/summary");
        return await res.json();
    }

    function renderTable(data) {
        transactionsTable.innerHTML = "";
        data.forEach(tx => {
            const row = transactionsTable.insertRow();
            row.innerHTML = `
                <td>${tx.date || "—"}</td>
                <td>${tx.category}</td>
                <td>${tx.amount || 0}</td>
                <td>${tx.body}</td>
            `;
        });
    }

    function renderCharts(summary) {
        const labels = summary.map(item => item.category);
        const counts = summary.map(item => item.count);
        const totals = summary.map(item => item.total_amount);

        new Chart(document.getElementById("barChart"), {
            type: "bar",
            data: {
                labels: labels,
                datasets: [{
                    label: "Transaction Count",
                    data: counts
                }]
            }
        });

        new Chart(document.getElementById("pieChart"), {
            type: "pie",
            data: {
                labels: labels,
                datasets: [{
                    label: "Total Amount",
                    data: totals
                }]
            }
        });
    }

    async function init() {
        const summary = await fetchSummary();
        renderCharts(summary);

        summary.forEach(item => {
            const opt = document.createElement("option");
            opt.value = item.category;
            opt.textContent = item.category;
            categorySelect.appendChild(opt);
        });

        const data = await fetchTransactions();
        renderTable(data);
    }

    categorySelect.addEventListener("change", async () => {
        const selected = categorySelect.value;
        const data = await fetchTransactions(selected);
        renderTable(data);
    });

    init();
});
