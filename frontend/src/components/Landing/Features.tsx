import React from "react";

const Features: React.FC = () => {
  const features = [
    {
      icon: "👥",
      title: "HR Management",
      description:
        "Manage employees, payroll, and performance all in one place with automated workflows.",
    },
    {
      icon: "💰",
      title: "Finance & Accounting",
      description:
        "Track expenses, generate invoices, and get real-time financial insights for better decisions.",
    },
    {
      icon: "📦",
      title: "Inventory Control",
      description:
        "Monitor stock levels, manage suppliers, and automate reordering with smart alerts.",
    },
    {
      icon: "🏢",
      title: "Multi-Tenant Ready",
      description:
        "Perfect for agencies and enterprises managing multiple companies or departments.",
    },
    {
      icon: "🔒",
      title: "Role-Based Access",
      description:
        "Control what each user can see and do with granular permission settings.",
    },
    {
      icon: "📊",
      title: "Advanced Analytics",
      description:
        "Get deep insights with customizable reports and real-time dashboards.",
    },
  ];

  return (
    <section id="features" className="py-20 bg-white">
      <div className="container mx-auto px-6">
        <div className="text-center mb-16">
          <h2 className="text-4xl font-bold text-gray-900 mb-4">
            Everything You Need to Scale
          </h2>
          <p className="text-xl text-gray-600 max-w-2xl mx-auto">
            Powerful features designed to help your business grow efficiently
            and effectively.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {features.map((feature, index) => (
            <div
              key={index}
              className="bg-gray-50 rounded-xl p-6 hover:shadow-lg transition-shadow"
            >
              <div className="text-3xl mb-4">{feature.icon}</div>
              <h3 className="text-xl font-semibold text-gray-900 mb-2">
                {feature.title}
              </h3>
              <p className="text-gray-600">{feature.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Features;
