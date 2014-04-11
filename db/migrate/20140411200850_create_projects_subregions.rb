class CreateProjectsSubregions < ActiveRecord::Migration
  def change
    create_table :projects_subregions, id: false do |t|
      t.belongs_to :project
      t.belongs_to :subregion
    end
    add_index(:projects_subregions, [:project_id, :subregion_id])
  end
end
