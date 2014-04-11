object @project

attributes :id,
           :title,
           :description,
           :status,
           :geography,
           :lead_department

# node(:geographies) { |project| project.geographies } unless locals[:hide_geographies]