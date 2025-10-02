import React from "react";

const StorySection: React.FC = () => {
  return (
    <section className="py-16 bg-white">
      <div className="container mx-auto px-6 max-w-6xl">
        <h2 className="text-3xl font-bold text-gray-900 mb-6">Our Story</h2>
        <p className="text-xl text-gray-600 leading-relaxed">
          While working with logistics and trading companies in East Africa, we
          observed the challenges that arise from fragmented operations—manual
          HR processes, untracked inventory, financial discrepancies, and
          inefficient workflow. Marjaan Solutions was born from a desire to
          empower companies with a unified digital platform that simplifies
          operations, increases productivity, and supports growth.
        </p>
      </div>
    </section>
  );
};

export default StorySection;
